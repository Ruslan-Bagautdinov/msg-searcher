from aiogram import Bot
from os import getenv

SERVER = getenv('SERVER', False)

if SERVER:
    BOT_TOKEN = getenv('BOT_TOKEN')
    APP_NAME = getenv('APP_NAME')
    SESSION_STRING = getenv('SESSION_STRING')
    MONEY_CHAT_ID = getenv('MONEY_CHAT_ID')
    ESTATE_CHAT_ID = getenv('ESTATE_CHAT_ID')

else:
    from config import *
    BOT_TOKEN = BOT_TOKEN
    APP_NAME = APP_NAME
    SESSION_STRING = SESSION_STRING
    MONEY_CHAT_ID = MONEY_CHAT_ID
    ESTATE_CHAT_ID = ESTATE_CHAT_ID

bot = Bot(
          token=BOT_TOKEN
         )
