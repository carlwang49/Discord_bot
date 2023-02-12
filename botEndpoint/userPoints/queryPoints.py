import discord
from config import bot
from loguru import logger
from db import get_session
from model import User_info
from botEndpoint.utils import get_points_message
import numpy as np

@bot.tree.command(name = "querypoints")
async def query_points(interaction : discord.Interaction):

    session = get_session()
    user = session.query(User_info).filter(User_info.user_id == interaction.user.id).first()

    if user:
        
        response = await get_points_message(user.points, query = True)
        await interaction.response.send_message(response, ephemeral = True)
    
    else:
        logger.error("No user found")