import discord
from config import Config

class Select_sugar(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label = Config.SUGAR[0], emoji="😋", value="正常甜"),
            discord.SelectOption(
                label = Config.SUGAR[1], emoji="😋", value="不要太甜"),
            discord.SelectOption(
                label = Config.SUGAR[2], emoji="😋", value="少糖"),
            discord.SelectOption(
                label = Config.SUGAR[3], emoji="😋", value="半糖"),
            discord.SelectOption(
                label = Config.SUGAR[4], emoji="😋", value="微糖"),
            discord.SelectOption(
                label = Config.SUGAR[5], emoji="😋", value="無糖")
        ]
        super().__init__(placeholder="請選擇甜度",
                         max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await self.view.respond_to_answer2(interaction, self.values)