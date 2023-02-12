from config import bot, Config
from datetime import datetime
from botEndpoint.customizedDrink.brand import Select_brand
import discord
import discord
from config import bot, Config
from discord.ext import tasks
from datetime import datetime, timedelta

@bot.tree.command(name="set_deadline")
async def set_deadline(interaction: discord.Interaction, am_pm: str, hour: int, min: int):

    if not interaction.user.get_role(int(Config.DIRECTOR_ID)):
        await interaction.response.send_message("您沒有權限使用這個功能", ephemeral = True)
        return

    now_hour = datetime.now().strftime('%H')
    now_min = datetime.now().strftime('%M')
    await interaction.response.send_message("現在時間 " + now_hour + ":" + now_min, ephemeral = True)
    print(hour, min)

    if hour < 0 or hour >= 12:
        await interaction.followup.send("請輸入正確格式! ", ephemeral = True)
        return
    elif min < 0 or min >= 60:
        await interaction.followup.send("請輸入正確格式! ", ephemeral = True)
        return
    else:
        pass
    if am_pm == "pm":
        hour += 12
    elif am_pm == "am":
        pass
    else:
        # 提醒使用者要輸入am或pm
        await interaction.followup.send("請輸入正確格式! (am / pm)", ephemeral = True)
        return
    # 新增時間限制
    if hour < int(now_hour):
        await interaction.followup.send("設定時間小於現在時間! ", ephemeral = True)
        return
    elif hour == int(now_hour) and min < int(now_min):
        await interaction.followup.send("設定時間小於現在時間! ", ephemeral = True)
        return
    else:

        print(hour, min)
        print(now_hour, now_min)
        pass

    Config.AM_PM = am_pm
    Config.END_TIME[0] = hour
    Config.END_TIME[1] = min
    Config.START_TIME[2] = datetime.now()
    Config.END_TIME[2] = datetime.now() + timedelta(hours = hour - datetime.now().hour) + timedelta(minutes = min - datetime.now().minute)

    from loguru import logger
    logger.warning(Config.START_TIME[2])
    logger.warning(Config.END_TIME[2])
    
    # 修改時：分(2位數)
    await interaction.followup.send("您設定的截止時間為:  " + str(am_pm) + " "+str(hour) + ":" + str("%02d" % min), ephemeral = True)

    view = Select_brand()
    await interaction.followup.send(view=view, ephemeral = True)
    await view.wait()
    ### 針對channel發送
    set_brand = Config.BRAND
    if set_brand == "五十嵐":
        file = discord.File("img/50嵐.jpg")
    if set_brand == "可不可":
        file = discord.File("img/kebuke.png")
    elif set_brand == "萬波":
        file = discord.File("img/wanpo.jpg")
    embed = discord.Embed(
        title="Hi all,", color=0x008cb4)
    embed.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/820/820603.png")
    embed.add_field(name="請點餐", value="輸入/order_drink進行點餐", inline=True)
    embed.set_footer(text="請注意截止請間為  "+str(hour) + ":" + str("%02d" % min))
    channel = bot.get_channel(Config.CHANNEL_ID)
    await channel.send(embed=embed)
    await channel.send(file=file)

    Config.ORDER_AVAL = True
    order_listener.start()

@tasks.loop(seconds = 10)
async def order_listener():

    if datetime.now().hour >= Config.END_TIME[0] and datetime.now().minute >= Config.END_TIME[1]:
        Config.ORDER_AVAL = False
        order_listener.stop()
        print("*********************************************")