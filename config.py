"""
This module loads configuration settings from environment variables using the `dotenv` library.
"""

from os import getenv

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

APP_NAME = getenv('APP_NAME')
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
USERNAME = getenv('USERNAME')
PHONE_NUMBER = getenv('PHONE_NUMBER')

BOT_NAME = getenv('BOT_NAME')
BOT_TOKEN = getenv('BOT_TOKEN')

SESSION_STRING = getenv('SESSION_STRING')
MONEY_CHAT_ID = int(getenv('MONEY_CHAT_ID'))
ESTATE_CHAT_ID = int(getenv('ESTATE_CHAT_ID'))
