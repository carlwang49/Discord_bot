import discord
from config import bot
from .workingUtils import help_embed

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(embed=help_embed(), ephemeral=True)

