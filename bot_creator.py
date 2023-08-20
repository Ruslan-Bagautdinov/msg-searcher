from aiogram import Bot
from os import getenv

SERVER = getenv('SERVER', False)

if SERVER:
    BOT_TOKEN = getenv('BOT_TOKEN')
    GROUP_CHAT_ID = getenv('GROUP_CHAT_ID')
    APP_NAME = getenv('APP_NAME')
    SESSION_STRING = getenv('SESSION_STRING')

else:
    from config import BOT_TOKEN, GROUP_CHAT_ID, APP_NAME, SESSION_STRING
    BOT_TOKEN = BOT_TOKEN
    GROUP_CHAT_ID = GROUP_CHAT_ID
    APP_NAME = APP_NAME
    SESSION_STRING = SESSION_STRING

bot = Bot(
          token=BOT_TOKEN
         )
