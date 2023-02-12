import discord
from config import bot, Config

@bot.tree.command(name="show_menu")
async def show_menu(interaction: discord.Interaction):

    if not Config.ORDER_AVAL:
        await interaction.response.send_message("現在尚未開始揪團, 請等飲料開團再下訂單", ephemeral = True)
        return

    set_brand = Config.BRAND
    if set_brand == "五十嵐":
        file = discord.File("img/50嵐.jpg")
    if set_brand == "可不可":
        file = discord.File("img/kebuke.png")
    elif set_brand == "萬波":
        file = discord.File("img/wanpo.jpg")

    await interaction.response.send_message(file=file, ephemeral = True)