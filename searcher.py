from pyrogram import Client, filters
import re

# own imports
from bot_creator import APP_NAME, SESSION_STRING

from sender import send_money, send_estate

from chats_money import CHATS_MONEY
from key_money import KEY_MONEY, WHITE_MONEY, BLACK_MONEY
from chats_estate import CHATS_ESTATE
from key_estate import KEY_ESTATE, WHITE_ESTATE, BLACK_ESTATE

from trie import Trie


class LastMessage:
    def __init__(self):
        self.last_message_money = 'last_message_money'
        self.last_message_estate = 'last_message_estate'


def create_filters(key_list, white_list, black_list):

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


key_money_filter, white_money_filter, black_money_filter = create_filters(KEY_MONEY, WHITE_MONEY, BLACK_MONEY)
key_estate_filter, white_estate_filter, black_estate_filter = create_filters(KEY_ESTATE, WHITE_ESTATE, BLACK_ESTATE)

chat_filter_money = filters.chat(CHATS_MONEY) & filters.text & key_money_filter
chat_filter_estate = filters.chat(CHATS_ESTATE) & filters.text & key_estate_filter


def searcher_main():
    
    def message_proceed(message):

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

    print('* * * Starting... * * *')
    app = Client(name=APP_NAME, session_string=SESSION_STRING, in_memory=True)
    last_message = LastMessage()
    print('* * * STARTED SUCCESSFULLY ! * * *')

    @app.on_message(chat_filter_money)
    async def find_money(client, message):

        if re.search(white_money_filter, message.text, re.IGNORECASE):

            if re.search(black_money_filter, message.text, re.IGNORECASE):
                pass
            elif message.text == last_message.last_message_money:
                pass
            else:
                last_message.last_message_money = message.text
                money_message = message_proceed(message)
                await send_money(money_message)

    @app.on_message(chat_filter_estate)
    async def find_estate(client, message):

        if re.search(white_estate_filter, message.text, re.IGNORECASE):

            if re.search(black_estate_filter, message.text, re.IGNORECASE):
                pass
            elif message.text == last_message.last_message_estate:
                pass
            else:
                last_message.last_message_estate = message.text
                estate_message = message_proceed(message)
                await send_estate(estate_message)

    app.run()
    print('* * * Pyrogram App Closed * * *')


if __name__ == "__main__":
    searcher_main()
