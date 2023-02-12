import discord
from config import Config

class Select_brand(discord.ui.View):

    @discord.ui.select(
        placeholder="請選擇你要開團的店家：",
        options=[
            # discord.SelectOption(label=jdata['50Lan'][1], emoji="🥤",description = "This is option 1!"),
            discord.SelectOption(
                label="五十嵐", emoji="🥤", value="五十嵐"),
            discord.SelectOption(
                label="可不可", emoji="🥤", value="可不可"),
            discord.SelectOption(
                label="萬波", emoji="🥤", value="萬波")
        ]
    )
    async def select_brand(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.brand = select_item.values[0]
        await interaction.response.send_message("你選擇的是：" + self.brand, ephemeral = True)
        self.children[0].disabled = True
        Config.BRAND = self.brand
        print(Config.BRAND)
        self.stop()