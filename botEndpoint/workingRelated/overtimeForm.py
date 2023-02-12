import discord
from discord import ui
import botEndpoint.workingRelated.selectionButton as sB
from .workingUtils import insert_overtime, welcome_overtime_embed, delete_overtime_embed, overtime_embed
from datetime import datetime
from botEndpoint.utils import get_points_message
from botEndpoint.userPoints import get_points

##############################################################################################################################
# Overtime From
##############################################################################################################################
# fill in the overtime sheet
class OvertimeSheet(ui.Modal, title='Overtime Sheet'):

    date = ui.TextInput(label='date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-1-1", required=True)
    project = ui.TextInput(label='project', style=discord.TextStyle.short,
                           placeholder="ex: tsmc project", required=True)
    department = ui.TextInput(
        label='department', style=discord.TextStyle.short, placeholder="ex: IT", required=True)
    hours = ui.TextInput(
        label='overtime', style=discord.TextStyle.short, placeholder="ex: 1~4", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        # store in database...
        await insert_overtime(interaction.user, interaction.user.id, self.date, self.project, self.hours, self.department)
        await interaction.response.send_message(content="update successfully !", view=sB.OvertimeSystemButton(), embed=welcome_overtime_embed(), ephemeral=True)
        
        year = datetime.now().year ; month = datetime.now().month ; day = datetime.now().day
        start_time = datetime.strptime(str(year) + str(month) + str(day) + "001500", "%Y%m%d%H%M%S")
        end_time = datetime.strptime(str(year) + str(month) + str(day + 1) + "000000", "%Y%m%d%H%M%S")

        points = await get_points(interaction.user.name, "揪團", start_time, end_time, datetime.now())
        message = await get_points_message(points, False)
        await interaction.followup.send(message, ephemeral = True)
# delete overtime sheet
class OvertimeSheetDelete(ui.Modal, title='Time Sheet'):

    date = ui.TextInput(label='date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-1-1", required=True)
    project = ui.TextInput(label='project', style=discord.TextStyle.short,
                           placeholder="ex: tsmc project", required=True)

    # submit
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=sB.OvertimeSystemButton(), embed=delete_overtime_embed(interaction.user.id, self.date, self.project), ephemeral=True)


# List overtime sheet
class OvertimeSheetList(ui.Modal, title='Overtime List'):

    date = ui.TextInput(label='date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-1-1", required=True)
    # submit

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=sB.OvertimeSystemButton(), embed=overtime_embed(interaction.user.id, self.date), ephemeral=True)