from botEndpoint.customizedDrink.items import Select_item
from botEndpoint.orderDrinkFlow.checkItem import checkitem
import discord
from config import Config

async def drinkFormula(interaction: discord.Interaction, name, End_hour, End_min):

    users = Config.TODAY_ORDERS
    End1 = str(End_hour)
    # 修改時：分(2位數)
    End2 = str("%02d" % End_min)
    view = Select_item()
    embed = discord.Embed(
        title="Hi,", description="請在下方選單選擇你想要的：", color=0x008cb4)
    embed.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/820/820603.png")
    embed.add_field(name="品項", value="菜單上的飲料", inline=True)
    embed.add_field(name="甜度", value="你想要的甜度", inline=True)
    embed.add_field(name="冰塊", value="請注意某些不供熱飲", inline=True)
    embed.set_footer(text="請注意截止請間為  "+End1+":"+End2)
    await interaction.followup.send(view=view, embed=embed)
    await view.wait()

    results = {
        "Name": name,
        "a1":  view.answer1,
        "a2":  view.answer2,
        "a3":  view.answer3,
    }
    a = view.answer1
    b = view.answer2
    c = view.answer3
    print(results)
    await interaction.followup.send(" ".join(results.get("Name")+results.get("a1")+results.get("a2")+results.get("a3")), ephemeral = True)
    await checkitem(interaction, a, b, c, users, name)