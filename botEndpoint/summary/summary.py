from config import Config, bot
import asyncio
import discord 
from discord import ui,app_commands
from discord.ext import commands
from datetime import datetime
import openai

openai.organization = Config.OPENAI_ORG
openai.api_key = Config.OPENAI_API_KEY

class SummaryModal(ui.Modal, title='Summary'):
    name = ui.TextInput(label='Title',style=discord.TextStyle.short)
    answer = ui.TextInput(label='Contents', style=discord.TextStyle.paragraph,required=True,max_length=1000)

    async def on_submit(self, interaction: discord.Interaction):
        # await interaction.response.defer()
        # print("Submitting")
        # response = await openai.Completion.acreate(
        #     model="text-davinci-003",
        #     prompt=f"{self.answer}",
        #     temperature=0.9,
        #     max_tokens=3000,
        #     # top_p=1.0,
        #     # frequency_penalty=0.0,
        #     # presence_penalty=0.0
        # )
        # response_dict = response.get("choices")
        # if response_dict and len(response_dict)>0:
        #     bot_message = response_dict[0]["text"]
        # embed = discord.Embed(title=self.title,description=f"{bot_message}",timestamp=datetime.now(),color=discord.Colour.blue())
        # embed.set_author(name=interaction.user,icon_url=interaction.user.avatar)
        # await interaction.followup.send(embed=embed)

        bot_message = self.answer
        await interaction.response.send_message(bot_message)

# @bot.listen()
# async def on_message(message:discord.Message):
#     # don't respond to ourselves
#     print(message.content)
#     if message.author == bot.user:
#         return
#     # if not bot.user.mentioned_in(message) or message.mention_everyone is True:
#     #     return
#     # if message.content.startswith(mention):
#     # await message.
#     # user_message = message.content[len(mention):]
#     print(message.content)
#     response = await openai.Completion.acreate(
#         model="text-davinci-003",
#         prompt=message.content,
#         # prompt=user_message,
#         temperature=0.9,
#         max_tokens=100,
#         # top_p=1.0,
#         # frequency_penalty=0.0,
#         # presence_penalty=0.0
#     )
#     # print(gptResponse)
#     response_dict = response.get("choices")
#     if response_dict and len(response_dict)>0:
#         bot_message = response_dict[0]["text"]
#     # print(bot_message)
#     await message.channel.send(bot_message)

# @tree.command(name="summary",description="整理重點(會議記錄、對話紀錄...等)")
# async def summary(interaction: discord.Interaction):
#     await interaction.response.send_modal(SummaryModal())

@bot.tree.command(name="summary",description="整理重點(會議記錄、對話紀錄...等)")
async def summary(interaction: discord.Interaction):
    print(interaction.channel_id)
    channel = bot.get_channel(interaction.channel_id)
    print(channel)
    messages = [f"{message.author.name}:{message.content}" async for message in channel.history(limit=20)]
    messages = messages[::-1]
    print(messages)

    await interaction.response.defer()
    print("Submitting")
    prompt = f"以下是聊天紀錄的陣列，包含使用者名稱與訊息內容，請幫我整理以下重點: {messages}"

    max_tokens = 4000 - 3*len(prompt)
    response = await openai.Completion.acreate(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=max_tokens,
        # top_p=1.0,
        # frequency_penalty=0.0,
        # presence_penalty=0.0
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict)>0:
        bot_message = response_dict[0]["text"]
    # embed = discord.Embed(title=self.title,description=f"{bot_message}",timestamp=datetime.now(),color=discord.Colour.blue())
    # embed.set_author(name=interaction.user,icon_url=interaction.user.avatar)
    # await interaction.followup.send(embed=embed)
    await interaction.followup.send(bot_message)

@bot.tree.command(name="hello",description="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello")


# @bot.command()
# async def response(ctx:commands.Context, input:str):
#     await ctx.send("response")