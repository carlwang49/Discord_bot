import discord
from discord import ui
import botEndpoint.workingRelated.selectionButton as sB
from datetime import datetime
from botEndpoint.utils import get_points_message
from botEndpoint.userPoints import get_points
from .workingUtils import insert_leavetime, welcome_leave_embed, delete_leave_embed, leave_embed

##############################################################################################################################
# Leave From
##############################################################################################################################
# Fill in Leavetime sheet
class LeavetimeSheet(ui.Modal, title='Leavetime Sheet'):

    apply_date = ui.TextInput(label='apply date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-1-1", required=True) 
    leave_date = ui.TextInput(label='leave date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-2-1", required=True)
    reason = ui.TextInput(label='reason', style=discord.TextStyle.short,
                          placeholder="ex: sick", required=True)
    department = ui.TextInput(
        label='department', style=discord.TextStyle.short, placeholder="ex: IT", required=True)
    hours = ui.TextInput(
        label='leavetime', style=discord.TextStyle.short, placeholder="ex: 1~8", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        # store in database...
        await insert_leavetime(interaction.user, interaction.user.id, self.apply_date, self.leave_date, self.reason, self.hours, self.department)
        await interaction.response.send_message(content="update successfully !", view= sB.LeaveSystemButton(), embed=welcome_leave_embed(), ephemeral=True)
        
        year = datetime.now().year ; month = datetime.now().month ; day = datetime.now().day
        start_time = datetime.strptime(str(year) + str(month) + str(day) + "001500", "%Y%m%d%H%M%S")
        end_time = datetime.strptime(str(year) + str(month) + str(day + 1) + "000000", "%Y%m%d%H%M%S")

        points = await get_points(interaction.user.name, "揪團", start_time, end_time, datetime.now())
        message = await get_points_message(points, False)
        await interaction.followup.send(message, ephemeral = True)

# Delete leavetime
class LeavetimeSheetDelete(ui.Modal, title='LeaveTime Sheet'):

    leave_date = ui.TextInput(label='leave date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-1-1", required=True)
    reason = ui.TextInput(label='reason', style=discord.TextStyle.short,
                          placeholder="ex: sick", required=True)

    # submit
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(view= sB.LeaveSystemButton(), embed=delete_leave_embed(interaction.user.id, self.leave_date, self.reason), ephemeral=True)


# List leavetime
class LeavetimeSheetList(ui.Modal, title='LeaveTime List'):

    leave_date = ui.TextInput(label='leave date', style=discord.TextStyle.short,
                        placeholder="ex: 2023-2-1", required=True)
    # submit

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(view= sB.LeaveSystemButton(), embed=leave_embed(interaction.user.id, self.leave_date), ephemeral=True)
