from discord import ButtonStyle, Button
from discord.ext import commands
from discord.ext import tasks
from discord import app_commands
import discord
from dotenv import load_dotenv
import os
import json
import asyncio
from discord import ui
import datetime
from config import Config

class Select_ice(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label = Config.ICE[0], emoji="🧊", value="正常冰"),
            discord.SelectOption(label = Config.ICE[1], emoji="🧊", value="少冰"),
            discord.SelectOption(label = Config.ICE[2], emoji="🧊", value="微冰"),
            discord.SelectOption(label = Config.ICE[3], emoji="🧊", value="去冰"),
            discord.SelectOption(label = Config.ICE[4], emoji="🧊", value="常溫"),
            discord.SelectOption(label = Config.ICE[5], emoji="🔥", value="熱"),
        ]
        super().__init__(placeholder="請選擇冰塊",
                         max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await self.view.respond_to_answer3(interaction, self.values)