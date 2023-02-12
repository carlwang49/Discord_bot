import discord
from config import bot
from loguru import logger
from db import get_session
from model import User_info
from botEndpoint.utils import get_points_message
import numpy as np
import re

@bot.tree.command(name = "register_email")
async def regsiter_email(interaction : discord.Interaction, *, email : str):
    
    session = get_session()
    user = session.query(User_info).filter(User_info.user_id == interaction.user.id).first()

    if not user.email:
        mouse_rule = re.findall(r'@', email)
        invalid_rule = re.findall(r'[\&\=\_\'\-\+\,\>\<' ']', email)
        email_rule = re.match(r'[0-9a-zA-Z]+@[0-9a-zA-Z\.]+', email)

        if len(mouse_rule) == 1 and len(invalid_rule) == 0 and email_rule.group(0) and email_rule.group(0) == email:
            user.email = email
            
            try:
                session.add(user)
                session.commit()
                await interaction.response.send_message("您的信箱註已註冊成功:man_gesturing_ok:", ephemeral = True)
            except Exception as e:
                logger.error("Session comitted failed")
                await interaction.response.send_message("您的信箱註冊失敗, 請洽詢伺服器管理員", ephemeral = True)

    elif user.email:
        logger.error("Users email has already registered")
        await interaction.response.send_message("您的信箱已經註冊過, 請使用您註冊的信箱來使用服務", ephemeral = True)
    else:
        logger.error("User not found")
        await interaction.response.send_message("您的會員資料尚未註冊, 請聯絡伺服器管理員", ephemeral = True)