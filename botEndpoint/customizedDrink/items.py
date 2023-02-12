import discord
from .sugar import Select_sugar
from .ice import Select_ice
from db import get_session
from model import Menu
from config import Config
import json

class Select_item(discord.ui.View):

    answer1 = None
    answer2 = None
    answer3 = None
    answer4 = None

    session = get_session()
    drinks = session.query(Menu).filter(Menu.brand == Config.BRAND).all()
    drinks = [drink.item for drink in drinks][:25]
    select_options = [discord.SelectOption(label = drink_name, emoji="🥤", value = drink_name) for drink_name in drinks]

    @discord.ui.select(
        placeholder = "請選擇你要的品項",
        options = select_options,
    )
    async def select_item(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.answer1 = select_item.values
        self.children[0].disabled = True
        sugar_select = Select_sugar()
        self.add_item(sugar_select)
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def respond_to_answer2(self, interaction: discord.Interaction, choices):
        self.answer2 = choices
        self.children[1].disabled = True
        ice_select = Select_ice()
        self.add_item(ice_select)
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def respond_to_answer3(self, interaction: discord.Interaction, choices):
        self.answer3 = choices
        self.children[2].disabled = True
        await interaction.message.edit(view=self)
        await interaction.response.defer()
        self.stop()