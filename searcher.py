"""
This module contains the main functionality for a Telegram bot that monitors specific chats for messages related to money exchange and apartment rentals. It uses Pyrogram for reading messages and Aiogram for sending messages based on predefined filters.
"""

import re

from aiogram import Bot
from pyrogram import Client, filters

from chats_estate import CHATS_ESTATE
from chats_money import CHATS_MONEY
# Own imports
from config import (APP_NAME,
                    BOT_TOKEN,
                    SESSION_STRING,
                    MONEY_CHAT_ID,
                    ESTATE_CHAT_ID)
from key_estate import KEY_ESTATE, WHITE_ESTATE, BLACK_ESTATE
from key_money import KEY_MONEY, WHITE_MONEY, BLACK_MONEY
from trie import Trie


class LastMessage:
    """
    A class to keep track of the last processed message for each category (money and estate).
    """

    def __init__(self):
        self.last_message_money = 'last_message_money'
        self.last_message_estate = 'last_message_estate'


def create_filters(key_list, white_list, black_list):
    """
    Create filters for messages based on key words, white list, and black list.

    :param key_list: List of key words to look for in messages.
    :param white_list: List of words that must be present in messages.
    :param black_list: List of words that must not be present in messages.
    :return: Tuple of filters (key_filter, white_filter, black_filter).
    """
    key_filter = filters.regex(f"({'|'.join(key_list)})", flags=re.IGNORECASE)

    white_trie = Trie()
    black_trie = Trie()

    for word in sorted(white_list):
        white_trie.add(word)
    for word in sorted(black_list):
        black_trie.add(word)

    white_filter = white_trie.pattern()
    black_filter = black_trie.pattern()

    return key_filter, white_filter, black_filter


def message_proceed(message):
    """
    Process the message to prepare it for sending.

    :param message: The message object from Telegram.
    :return: A formatted string containing the message details.
    """
    message_for_bot = ''
    message_for_bot += f'{message.link}\n'
    message_for_bot += f'{message.text}\n'

    if message.chat.title:
        message_for_bot += f'Chat: {message.chat.title}\n'
    if message.from_user.username:
        message_for_bot += f'Username: {message.from_user.username}\n'
    if message.from_user.first_name:
        message_for_bot += f'First_name: {message.from_user.first_name}\n'
    if message.from_user.last_name:
        message_for_bot += f'Last_name: {message.from_user.last_name}\n'
    if message.from_user.phone_number:
        message_for_bot += f'Phone_number: {message.from_user.phone_number}\n'
    return message_for_bot


async def send_message_to_chat(bot, chat, message):
    """
    Send a message to a specified chat.

    :param bot: The bot instance.
    :param chat: The chat ID where the message will be sent.
    :param message: The message to be sent.
    """
    await bot.send_message(chat, message)


def searcher_main():
    """
    Main function to start the message monitoring and processing.
    """

    async def find_message(client,
                           message,
                           white_filter,
                           black_filter,
                           last_message,
                           bot,
                           chat):
        """
        Process a message to determine if it should be forwarded based on filters.

        :param client: The Pyrogram client instance.
        :param message: The message object from Telegram.
        :param white_filter: The filter for words that must be present.
        :param black_filter: The filter for words that must not be present.
        :param last_message: The LastMessage instance to track the last processed message.
        :param bot: The Aiogram bot instance.
        :param chat: The chat ID where the message will be sent if it passes the filters.
        """
        if re.search(white_filter, message.text, re.IGNORECASE):
            if re.search(black_filter, message.text, re.IGNORECASE):
                pass
            elif message.text == last_message.last_message_money:
                pass
            else:
                last_message.last_message_money = message.text
                money_message = message_proceed(message)
                await send_message_to_chat(bot, chat, money_message)

    print('* * * Starting... * * *')

    key_money_filter, white_money_filter, black_money_filter = create_filters(KEY_MONEY, WHITE_MONEY, BLACK_MONEY)
    key_estate_filter, white_estate_filter, black_estate_filter = create_filters(KEY_ESTATE, WHITE_ESTATE,
                                                                                 BLACK_ESTATE)
    chat_filter_money = filters.chat(CHATS_MONEY) & filters.text & key_money_filter
    chat_filter_estate = filters.chat(CHATS_ESTATE) & filters.text & key_estate_filter

    print('* * * Filters created OK... * * *')

    app = Client(name=APP_NAME, session_string=SESSION_STRING, in_memory=True)
    print('* * * Pyrogram app started... * * *')
    bot = Bot(token=BOT_TOKEN)
    print('* * * Aiogram bot started... * * *')
    last_message = LastMessage()
    print('* * * STARTED SUCCESSFULLY ! * * *')

    @app.on_message(chat_filter_money)
    async def find_money(client, message):
        await find_message(client,
                           message,
                           white_money_filter,
                           black_money_filter,
                           last_message,
                           bot,
                           MONEY_CHAT_ID)

    @app.on_message(chat_filter_estate)
    async def find_estate(client, message):
        await find_message(client,
                           message,
                           white_estate_filter,
                           black_estate_filter,
                           last_message,
                           bot,
                           ESTATE_CHAT_ID)

    app.run()
    print('* * * Pyrogram App Closed * * *')


if __name__ == "__main__":
    searcher_main()
