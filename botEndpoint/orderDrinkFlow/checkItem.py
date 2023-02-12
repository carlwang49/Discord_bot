from config import Config
from botEndpoint.userPoints import get_points
from datetime import datetime
import botEndpoint.utils as util
from botEndpoint.utils import get_points_message
import discord

class Check_item(discord.ui.View):
    check = 0

    def __init__(self) -> None:
        super().__init__()
        self.value = None

    foo: bool = None

    @ discord.ui.button(label="確認",
                        style=discord.ButtonStyle.blurple)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("已確認", ephemeral = True)
        self.foo = True
        self.check = 1
        self.stop()

    @ discord.ui.button(label="取消",
                        style=discord.ButtonStyle.red)
    async def reject(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("已取消", ephemeral = True)
        self.foo = True
        self.check = 0
        self.stop()

async def checkitem(interaction: discord.Interaction, answer1, answer2, answer3, users, name):
    view = Check_item()
    await interaction.followup.send(view=view,  ephemeral = True)
    await view.wait()
    checkOK = view.check

    if checkOK == 1:

        Config.TODAY_ORDERS = await util.update_data(users, interaction.user, answer1)
        Config.TODAY_ORDERS = await util.add_content(users, interaction.user, name, answer1, answer2, answer3)
        points = await get_points(interaction.user.name, "揪團", Config.START_TIME[2], Config.END_TIME[2], datetime.now())
        message = await get_points_message(points, False)
        await interaction.followup.send(message, ephemeral = True)
    else:
        return