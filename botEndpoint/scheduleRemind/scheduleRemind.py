import discord
from config import bot, Config
from loguru import logger
from db import get_session
from model import User_info, Emoji_info
import numpy as np
from discord.ext import commands, tasks
from botEndpoint.utils import calendar_setting
from datetime import datetime, timedelta
import re

@tasks.loop(seconds = Config.SCHEDULE_TIME)
async def schedule_remind():

    session = get_session()

    try:
        service = await calendar_setting()
    except Exception as e:
        logger.error(f"Error : {e}")
        return

    users = session.query(User_info).all()

    clock = session.query(Emoji_info).filter(Emoji_info.emoji_name == 'clock').first()
    emoji_clock = f"<:{clock.emoji_eng}:{clock.emoji_id}>"

    for user in users:
        if user.email:
            # Call the Calendar API
            now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            logger.info('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId= user.email, timeMin=now, #calendarId = primary, 代表取得現在登入使用者的 calendarId
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                logger.error('No upcoming events found.')
                continue

            # Prints the start and name of the next 10 events
            for event in events:
                # 2022-10-20T15:00:00+08:00
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))

                start_time = re.split(r"[T|:|+|-]", start)
                end_time = re.split(r"[T|:|+|-]", end)

                start_time = "".join(start_time[:-2])
                end_time = "".join(end_time[:-2])

                start_time = datetime.strptime(start_time,"%Y%m%d%H%M%S")
                end_time = datetime.strptime(end_time,"%Y%m%d%H%M%S")

                earliness = timedelta(hours = 12)

                logger.warning(event)
                if True:#datetime.now() >= start_time - earliness and datetime.now() <= start_time - earliness + timedelta(seconds = Config.SCHEDULE_TIME):
                    
                    title_msg = f"行程通知提醒: {event['summary']}" if "summary" in event else "行程通知提醒:"
                    event_msg = f"您在 12 小時過後, 已安排 **{event['summary']}**." if "summary" in event else f"您在 12 小時過後, 已安排一項活動."
                    time_msg =  f"活動時間 : **{start_time} 至 {end_time}**."
                    location_msg = f"活動地點 : **{event['location']}**." if "location" in event else ""
                    warm_msg = f"要記得哦！！不然本機器人不會再提醒你一次QQ:robot:"

                    embed = discord.Embed(title = title_msg, colour = discord.Color.random())
                    embed.add_field(name = "安排行程:", value = event_msg, inline = False)
                    embed.add_field(name = f"{emoji_clock}時間:", value = time_msg, inline = False)
                    embed.add_field(name = ":cityscape:地點:", value = location_msg, inline = False)
                    embed.add_field(name = "溫馨提醒:", value = warm_msg, inline = False)

                    if len(str(user.user_id)) == 18:
                        send_user = bot.get_user(user.user_id)
                        await send_user.send(embed = embed)
                    else:
                        channel = bot.get_channel(user.user_id)
                        await channel.send(embed = embed)

                    logger.info(f"Start time : {start_time}")
                    logger.info(f"End time : {end_time}")
                
                # start_day = start_token[0]
                # start_hour = int(start_token[1])
                # end_day =  end_token[0]
                # end_hour = int(end_token[1])

                # logger.warning(f"[Event] : {event}")
                # logger.info(f"Start token : {start_token}")
                # logger.info(f"End token : {end_token}")