from config import bot
import botEndpoint.userPoints.pointUtils as pU
import botEndpoint.userPoints.paginatorView as pV
import discord

@bot.tree.command(name="mall")
async def roles(interaction: discord.Interaction):

    embeds = pU.get_mall_embeds()
    view = pV.PaginatorView(embeds)
    await interaction.response.send_message(embed=view.initial, view=view)