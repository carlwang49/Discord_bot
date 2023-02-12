import discord
from model import *
from discord import ui
import botEndpoint.userPoints.paginatorView as pV
import botEndpoint.userPoints.pointUtils as pU

# purchase sheet
class Purchase(ui.Modal, title='Purchase'):

    commodity = ui.TextInput(label='commodity', style=discord.TextStyle.short,
                             placeholder="ex: bicycle", required=True)
    commodity_points = ui.TextInput(label='Commodity_Points', style=discord.TextStyle.short,
                                    placeholder="ex: 3000", required=True)

    # submit
    async def on_submit(self, interaction: discord.Interaction):

        flag = pU.check_wallet(interaction.user.id, self.commodity_points)

        if flag:
            pU.purchase(interaction.user.id, self.commodity,
                     self.commodity_points)
            embeds = pU.get_mall_embeds()
            view = pV.PaginatorView(embeds)
            await interaction.response.send_message(embed=view.initial, view=view)
        else:
            embeds = pU.get_mall_embeds()
            view = pV.PaginatorView(embeds)
            await interaction.response.send_message("Sorry, insufficient points...", embed=view.initial, view=view)

