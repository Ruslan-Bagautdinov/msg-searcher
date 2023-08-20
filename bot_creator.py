from aiogram import Bot
from os import getenv

SERVER = getenv('SERVER', False)

if SERVER:
    BOT_TOKEN = getenv('BOT_TOKEN')
    URI_APP = getenv('URI_APP')
    GROUP_CHAT_NAME = getenv('GROUP_CHAT_NAME')
    GROUP_CHAT_ID = getenv('GROUP_CHAT_ID')

else:
    from config import *
    BOT_TOKEN = BOT_TOKEN
    URI_APP = URI_APP
    GROUP_CHAT_NAME = GROUP_CHAT_NAME
    GROUP_CHAT_ID = GROUP_CHAT_ID

bot = Bot(
          token=BOT_TOKEN
         )
