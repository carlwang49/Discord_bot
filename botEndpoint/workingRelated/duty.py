import discord
from config import bot
from .selectionButton import SystemProtal
from .workingUtils import welcome_embed

@bot.tree.command(name="duty", description="Select your service")
async def duty(interaction: discord.Interaction):
    await interaction.response.send_message(content="Select your service", view=SystemProtal(), ephemeral=True, embed=welcome_embed())
