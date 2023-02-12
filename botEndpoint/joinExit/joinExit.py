from discord.ext import commands, tasks
from dataclasses import dataclass
from config import Config
from config import bot
from model import User_info, Event_points
from db import get_session
from loguru import logger


@bot.event
async def on_member_join(member):

    session = get_session()
    user = session.query(User_info).filter(User_info.user_id == str(member.id)).first()
    
    if not user:
        try:
            new_user = User_info(
                    name = member.name,
                    user_id = member.id,
                    points = 300, # Initial points
                )
            session.add(new_user)
            session.commit()   

            new_user_event = Event_points(
                name = member.name,
                user_id = member.id,
                team_buying = 0,
                working_report = 0,
                docs_apply = 300, # Initial points
            )
            session.add(new_user_event)
            session.commit()
            
        except Exception as e:
            logger.warning(f"Session commit error : {e}")

        join_msg = member.name + ", Welcome to this server... Say HI to your homie here!!"
        channel = bot.get_channel(Config.CHANNEL_ID)
        await channel.send(join_msg)


@bot.event
async def on_member_remove(member):

    session = get_session()
    user_event = session.query(Event_points).filter(Event_points.user_id == str(member.id)).first()
    user = session.query(User_info).filter(User_info.user_id == str(member.id)).first()
    
    if user and user_event:
        try:
            session.delete(user_event)
            session.delete(user)
            session.commit()
        except Exception as e:
            logger.warning(f"Session commit error : {e}")

        exit_msg = member.name + " has left here... Plz pray for him/her"
        channel = bot.get_channel(Config.CHANNEL_ID)
        await channel.send(exit_msg)