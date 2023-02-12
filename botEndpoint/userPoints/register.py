import discord
from discord import ui
from config import bot
from .pointUtils import insert_user_info

class Register(ui.Modal, title='Register'):

    user = ui.TextInput(label='user', style=discord.TextStyle.short,
                        placeholder="ex: Carl", required=True)
    title = ui.TextInput(label='title', style=discord.TextStyle.short,
                         placeholder="ex: Senior Engineer", required=True)
    department = ui.TextInput(
        label='department', style=discord.TextStyle.short, placeholder="ex: IT", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        # store in database...
        await insert_user_info(interaction.user, interaction.user.id, self.title, self.department)
        await interaction.response.send_message(content="Register successfully !", ephemeral=True)

@bot.tree.command(name="register")
async def register(interaction: discord.Interaction):
    await interaction.response.send_modal(Register())