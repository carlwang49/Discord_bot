from config import bot, Config
import discord

@bot.tree.command(name="show_drink_orders")
async def show_drink_orders(interaction: discord.Interaction):
    
    if not Config.ORDER_AVAL:
        await interaction.response.send_message("現在尚未開始揪團, 請等飲料開團再下訂單", ephemeral = True)
        return

    users = Config.TODAY_ORDERS
    num = len(users["TodayOrder"])
    print("Number", num)
    order = []
    for i in range(0, num):
        name = users["TodayOrder"][i]["Name"][0]
        item = users["TodayOrder"][i]["item"][0]
        sugar = users["TodayOrder"][i]["Sugar"][0]
        ice = users["TodayOrder"][i]["ice"][0]
        tmp = (name+":  "+item+" | "+sugar+" "+ice)
        order.append(tmp)

    print(order)

    if any(order):
        await interaction.response.send_message("\n".join('%s' % id for id in order), ephemeral = True)
    else:
        await interaction.response.send_message("現在還沒有人點任何飲料哦:beers:", ephemeral = True)