from config import bot
import discord
from datetime import datetime
from .drinkFormula import drinkFormula
from config import Config

async def menu(interaction: discord.Interaction, name, End_hour, End_min):
    if Config.BRAND == "五十嵐":
        file = discord.File("img/50嵐.jpg")
    if Config.BRAND == "可不可":
        file = discord.File("img/kebuke.png")
    elif Config.BRAND == "萬波":
        file = discord.File("img/wanpo.jpg")
    await interaction.response.send_message(file=file, ephemeral = True)
    await drinkFormula(interaction, name, End_hour, End_min)

@bot.tree.command(name="order_drinks")
async def order_drinks(interaction: discord.Interaction, 名稱: str):

    if not Config.ORDER_AVAL:
        await interaction.response.send_message("現在尚未開始揪團, 請等飲料開團再下訂單", ephemeral = True)
        return

    name = [名稱]
    now_hour = datetime.now().strftime('%H')
    now_min = datetime.now().strftime('%M')

    End_hour = Config.END_TIME[0]
    End_min = Config.END_TIME[1]
    Start_hours = int(now_hour)
    Start_min = int(now_min)

    await menu(interaction, name, End_hour, End_min)