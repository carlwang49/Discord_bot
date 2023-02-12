import discord
from config import bot
from db import get_session
from model import User_info, Event_points
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import scipy.stats
from loguru import logger
from random import randint
from config import Config
import math

@bot.tree.command(name = "lottery")
async def lottery(interaction : discord.Interaction):

    if not interaction.user.get_role(int(Config.DIRECTOR_ID)):
        await interaction.response.send_message(f"您沒有權限使用這個功能", ephemeral = True)
        return
        
    session = get_session()
    matching_level = 10

    # 1. T-score evaluation (用於放入數字做 random 的基底)
    users = session.query(User_info).all()
    users_points = np.asarray([user.points for user in users])

    std = np.std(users_points)
    mean = np.mean(users_points)
    standarlized_points = [(points - mean) / std for points in users_points]
    T_scores =  np.asarray([int(z_score * 30 + 170) for z_score in standarlized_points])

    # 2. Kmeans
    all_ep_row = session.query(Event_points).all()
    event_name = [column.key for column in Event_points.__table__.columns if column.key not in ["name", "user_id"]]
    event_points = []
    user_label = [-1 for _ in range(len(all_ep_row))]

    # Data preprocessing (Extract each points)
    for user in all_ep_row:
        user_each_points = []
        for event in event_name:
            user_each_points.append(user.__getattribute__(event))
        event_points.append(user_each_points)

    # Kmeans with Pearson and Cosine similarity
    kmeans_fit = KMeans(n_clusters = matching_level).fit(event_points)
    
    pearson_threshold = 0.95
    for idx, event_point in enumerate(event_points):

        max_cur_pears = -1000
        max_pears_label = -1
        max_centroid = None
        for label, centroid in enumerate(kmeans_fit.cluster_centers_):
            pearson_cor, _ = scipy.stats.pearsonr(event_point, centroid)

            if pearson_cor > max_cur_pears:
                max_cur_pears = pearson_cor
                max_pears_label = label
                max_centroid = centroid
        
        if max_cur_pears >= pearson_threshold:
            
            if max_pears_label == kmeans_fit.labels_[idx]:
                user_label[idx] = max_pears_label
            else:
                k_center_dist = euclidean_distances(kmeans_fit.cluster_centers_[kmeans_fit.labels_[idx]][None, :], np.asarray(event_point)[None, :])
                pearson_dist = euclidean_distances(max_centroid[None, :], np.asarray(event_point)[None, :])

                if k_center_dist >= pearson_dist:
                    user_label[idx] = kmeans_fit.labels_[idx]
                else:
                    # logger.warning("Pearson working!!!")
                    user_label[idx] = max_pears_label

    
    # 3. reassign level
    sorting_index = sorted(range(len(kmeans_fit.cluster_centers_)), key = lambda k : sum(kmeans_fit.cluster_centers_[k]))

    for idx in range(len(user_label)):
        user_label[idx] = sorting_index[user_label[idx]] + 1

    # 4. Lotterying Now!!!
    black_box = []
    for level, t_score in zip(user_label, T_scores):
        for  _ in range(t_score * int(math.pow(level, 3))):
            black_box.append(level)

    user_info = np.asarray([[user.name, user.user_id] for user in users])
    black_box = np.asarray(black_box)
    np.random.shuffle(black_box)

    # 4-1 Choose group
    lucky_group = black_box[randint(0, len(black_box) - 1)]
    group_member = user_info[np.argwhere(user_label == lucky_group).flatten()]
    group_points = users_points[np.argwhere(user_label == lucky_group).flatten()]

    # 4-2 Chosse lucky man
    lucky_number = randint(0, len(group_member) - 1)
    lucky_man = group_member[lucky_number]
    man_points = group_points[lucky_number]


    # for k in range(10):
    #     print(f"Count {k} = {list(black_box).count(k)}")
        
    logger.info(f"Choosen group : {lucky_group}")
    logger.info(f"Lucky man name : {lucky_man[0]}")
    logger.info(f"Lucky man id : {lucky_man[1]}")
    logger.info(f"Lucky man points : {man_points}, Maximum points : {max(users_points)}, Minimum points : {min(users_points)}")

    await interaction.response.send_message(f":fireworks::fireworks::fireworks:** 恭喜幸運兒 {lucky_man[0]} 獲得頭獎！！！** :fireworks::fireworks::fireworks:")