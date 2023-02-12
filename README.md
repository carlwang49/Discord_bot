# WorkEASE bot 

Introducing our latest Discord bot, designed to simplify and streamline your daily workplace routine. With our bot, you can now keep track of your work schedule, request time off, order drinks and food, and more.

Our bot features a convenient work log system, allowing you to easily document your daily tasks and communicate them to your supervisor. This makes it simple to stay on top of your responsibilities and keep track of your progress.

We also offer a seamless ordering system, making it easy to order drinks and food without leaving the Discord platform. Our bot integrates with Uber to ensure that your orders arrive quickly and efficiently.

In addition, our bot integrates with ChatGPT, allowing you to take advantage of its advanced language processing capabilities. This makes it possible to use our bot to take meeting minutes, track customer requirements, and more.

Finally, our bot also includes a feedback mechanism, in the form of a lottery system. This rewards our users for their continued support and engagement, and helps keep the platform lively and dynamic.

[![Package Version](https://img.shields.io/pypi/v/chatterbot.svg)](https://pypi.python.org/pypi/chatterbot/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/gunthercox/ChatterBot.svg?branch=master)](https://travis-ci.org/gunthercox/ChatterBot)
[![Documentation Status](https://readthedocs.org/projects/chatterbot/badge/?version=stable)](http://chatterbot.readthedocs.io/en/stable/?badge=stable)
[![Coverage Status](https://img.shields.io/coveralls/gunthercox/ChatterBot.svg)](https://coveralls.io/r/gunthercox/ChatterBot)
[![Code Climate](https://codeclimate.com/github/gunthercox/ChatterBot/badges/gpa.svg)](https://codeclimate.com/github/gunthercox/ChatterBot)
[![Join the chat at https://gitter.im/chatterbot/Lobby](https://badges.gitter.im/chatterbot/Lobby.svg)](https://gitter.im/chatterbot/Lobby?utm_source=badge&utm_medium=badge&utm_content=badge)

An example of typical input would be something like this:

> **user:** /hello  
> **bot:**  I am doing very well, thank you for asking.  

## Installation

```Python3
git clone https://github.com/hongpei100/NetDB_DiscordBot.git
```
```
docker compsoe up
```

## Config setting

```
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
import discord

load_dotenv()

bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "1"))
    MAX_SESSION_MINUTES = int(os.environ.get("MAX_SESSION_MINUTES", "1"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    HATE_WORD = os.environ.get("HATE_WORD", [])
```

### Features:

This template comes in with many in-built useful and flexible features, such as

#### • **Beverage Ordering**

- /order_drinks
- /show_menu
- /shor_drink_orders

#### • **Human Resource Management System (HRM)**

- /duty
<img width="544" alt="image" src="https://user-images.githubusercontent.com/40038409/218241115-1dc09656-5297-4179-815b-9ac0738b9c9a.png">

#### • **Meeting arrangement**

- /speechtosummary
- /speechtotext
<img width="1318" alt="image" src="https://user-images.githubusercontent.com/40038409/218241725-3b69120f-8556-4a9c-83d1-908a9fd69b28.png">

- /summary
<img width="992" alt="image" src="https://user-images.githubusercontent.com/40038409/218241011-7adf6add-07ff-46d4-9631-b06202d056d0.png">
<img width="378" alt="image" src="https://user-images.githubusercontent.com/40038409/218241039-3594d23a-5d17-4781-b665-ca978b776fb6.png">

#### • **Bonus system**

- /lottery
- /querypoints
- /mall
<img width="544" alt="image" src="https://user-images.githubusercontent.com/40038409/218241335-82d37d9e-93bf-4c33-9ca7-6d9c134c4512.png">






