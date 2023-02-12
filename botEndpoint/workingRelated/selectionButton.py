import discord
import botEndpoint.workingRelated.timeSheetForm as tS#from .timeSheetForm import TimeSheet, TimeSheetDelete, TimeSheetList
import botEndpoint.workingRelated.overtimeForm as oF#overtimeForm#from .overtimeForm import OvertimeSheet, OvertimeSheetDelete, OvertimeSheetList
import botEndpoint.workingRelated.leaveForm as lF#from .leaveForm import LeavetimeSheet, LeavetimeSheetDelete, LeavetimeSheetList
import botEndpoint.workingRelated.selectionButton as sB
from .workingUtils import welcome_overtime_embed, welcome_timesheet_embed, still_in_develop_embed, welcome_embed, welcome_leave_embed

##############################################################################################################################
# ----Selection----
##############################################################################################################################
# Entrance Protal
class SystemProtal(discord.ui.View):

    options = [
        discord.SelectOption(label="Timesheet System",
                             value="1", description="Records the amount of time an employee works on tasks"),
        discord.SelectOption(
            label="Leave System/Overtime System", value="2", description="Manage employees time-off/overtime requests"),
        discord.SelectOption(label="Application System",
                             value="3", description="Require for certain apply form")
    ]

    @discord.ui.select(placeholder="Choose your system", options=options)
    async def menu_callback(self, interaction: discord.Interaction, select):
        select.disable = True
        if select.values[0] == "1":
            await interaction.response.send_message(embed=welcome_timesheet_embed(), view=TimeSheetButton(), ephemeral=True)
        elif select.values[0] == "2":
            # !!!!
            await interaction.response.send_message(view=PickButton(), ephemeral=True)
        elif select.values[0] == "3":
            # !!!!
            await interaction.response.send_message(embed=still_in_develop_embed(), view=SystemProtal(), ephemeral=True)

##############################################################################################################################
# ----buttons----
##############################################################################################################################
# TimeSheet button
class TimeSheetButton(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✎ Fill in", style=discord.ButtonStyle.blurple)
    async def fill(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(tS.TimeSheet())

    @discord.ui.button(label="✘ Delete", style=discord.ButtonStyle.danger)
    async def delete(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(tS.TimeSheetDelete())

    @discord.ui.button(label="≡ List", style=discord.ButtonStyle.green)
    async def list(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(tS.TimeSheetList())

    @discord.ui.button(label="⏎ back", style=discord.ButtonStyle.grey)
    async def back(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message(embed=welcome_embed(), view=SystemProtal(), ephemeral=True)


# Pick Overtime or Leavetime system button
class PickButton(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="➠ OvertimeSystem", style=discord.ButtonStyle.secondary)
    async def test(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message(embed=welcome_overtime_embed(),view = sB.OvertimeSystemButton(), ephemeral=True)

    @discord.ui.button(label="➠ Leave System", style=discord.ButtonStyle.secondary)
    async def test2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message(embed=welcome_leave_embed(),view=LeaveSystemButton(), ephemeral=True)


# Overtime System button
class OvertimeSystemButton(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✎ Fill in overtime", style=discord.ButtonStyle.blurple)
    async def test(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(oF.OvertimeSheet())

    @discord.ui.button(label="✘ Delete overtime", style=discord.ButtonStyle.danger)
    async def test2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(oF.OvertimeSheetDelete())

    @discord.ui.button(label="≡ List overtime", style=discord.ButtonStyle.green)
    async def list(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(oF.OvertimeSheetList())

    @discord.ui.button(label="⏎ back", style=discord.ButtonStyle.grey)
    async def back(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message(embed=welcome_embed(), view=SystemProtal())


# Leave System button
class LeaveSystemButton(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✎ Fill in leavetime", style=discord.ButtonStyle.blurple)
    async def fill_leave(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(lF.LeavetimeSheet())

    @discord.ui.button(label="✘ Delete leavetime", style=discord.ButtonStyle.danger)
    async def delete_leave(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(lF.LeavetimeSheetDelete())

    @discord.ui.button(label="≡ List leavetime", style=discord.ButtonStyle.green)
    async def list_leave(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(lF.LeavetimeSheetList())

    @discord.ui.button(label="⏎ back", style=discord.ButtonStyle.grey)
    async def back(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message(embed=welcome_embed(), view=SystemProtal(), ephemeral=True)