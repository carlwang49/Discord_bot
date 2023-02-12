from discord.ext import commands, tasks
from dataclasses import dataclass
import datetime
import discord
from discord import app_commands
from config import Config
from config import bot
from datetime import datetime, timedelta
from loguru import logger
from db import get_session
from model import User_info
import numpy as np

async def get_points(user_name : str, event: str, start : datetime, end : datetime, finish_time : datetime):

    match event:
        case "揪團" | "工時回報":
            duration = timedelta(minutes = end.minute - start.minute)
            spend_time = timedelta(minutes = finish_time.minute - start.minute)

            try:
                percent = 1 - (spend_time / duration)
            except Exception as e:
                logger.error(e)
                return

        case "請假":
            spend_day = timedelta(days = end.day - start.day).days
        case _:
            logger.error("Unknown event")
            return

    match event:
        case "揪團":
            match percent:
                case _ if percent >= 0.88: # 頂標
                    gaussian_white_noise = int(np.random.normal(40, 20, size = 1))
                    point = np.random.randint(200, 400) + gaussian_white_noise
                case _ if percent >= 0.75: # 前標
                    gaussian_white_noise = int(np.random.normal(30, 15, size = 1))
                    point = np.random.randint(100, 200) + gaussian_white_noise
                case _ if percent >= 0.50: # 均標
                    point = 50
                case _ if percent >= 0.25: # 後標
                    point = 0
                case _ if percent >= 0.12: # 底標
                    point = -30
                case _ if percent >= 0: # 不如底標
                    point = -60
                case _:
                    logger.error(f"Event {event} has negative point....")
                    return

        case "工時回報":
            match percent:
                case _ if percent >= 0.88: # 頂標
                    gaussian_white_noise = int(np.random.normal(5, 1, size = 1))
                    point = np.random.randint(40, 50) + gaussian_white_noise
                case _ if percent >= 0.75: # 前標
                    gaussian_white_noise = int(np.random.normal(10, 5, size = 1))
                    point = np.random.randint(20, 40) + gaussian_white_noise
                case _ if percent >= 0.50: # 均標
                    point = 50
                case _ if percent >= 0.25: # 後標
                    point = 0
                case _ if percent >= 0.12: # 底標
                    point = -30
                case _ if percent >= 0: # 不如底標
                    point = -60
                case _:
                    logger.error(f"Event {event} has negative point....")
                    return

        case "請假":
            match spend_day:
                case _ if spend_day >= 90: # 頂標
                    point = -(spend_day * 4 / 12 * 4)
                case _ if spend_day >= 30 and spend_day < 90: # 前標
                    point = -(spend_day * 4 / 4 * 4)
                case _ if spend_day >= 14 and spend_day < 30: # 均標
                    point = -(spend_day * 4 / 2 * 4)
                case _ if spend_day >= 7 and spend_day < 14: # 後標
                    point = -(spend_day * 4 / 1 * 4)
                case _ if spend_day < 7: # 底標
                    point = -(spend_day * 4 / 0.5 * 4)
        case _:
            logger.error("Unknown event")
            return

    session = get_session()
    user = session.query(User_info).filter(User_info.name == user_name).first()

    if user:
        user.points += point

        try:
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(e)
    
    return point

