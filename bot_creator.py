from aiogram import Bot
from os import environ

SERVER = environ.get('SERVER', default=False)

if SERVER:
    BOT_TOKEN = environ.get('BOT_TOKEN')
    APP_NAME = environ.get('APP_NAME')
    SESSION_STRING = environ.get('SESSION_STRING')
    MONEY_CHAT_ID = environ.get('MONEY_CHAT_ID')
    ESTATE_CHAT_ID = environ.get('ESTATE_CHAT_ID')

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
