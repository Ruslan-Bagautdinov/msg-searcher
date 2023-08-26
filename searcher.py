from pyrogram import Client, filters
import re

from icecream import ic

# own imports
from bot_creator import APP_NAME, SESSION_STRING

from sender import send_money, send_estate

from key_money import CHATS_MONEY, KEY_MONEY, WHITE_MONEY, BLACK_MONEY
from key_estate import CHATS_ESTATE, KEY_ESTATE, WHITE_ESTATE, BLACK_ESTATE
from trie import Trie


key_money_filter = filters.regex(f"({'|'.join(KEY_MONEY)})", flags=re.IGNORECASE)
key_estate_filter = filters.regex(f"({'|'.join(KEY_ESTATE)})", flags=re.IGNORECASE)

white_trie_money = Trie()
black_trie_money = Trie()
for word in sorted(WHITE_MONEY):
    white_trie_money.add(word)
for word in sorted(BLACK_MONEY):
    black_trie_money.add(word)
white_money_filter = white_trie_money.pattern()
black_money_filter = black_trie_money.pattern()

white_trie_estate = Trie()
black_trie_estate = Trie()
for word in sorted(WHITE_ESTATE):
    white_trie_estate.add(word)
for word in sorted(BLACK_ESTATE):
    black_trie_estate.add(word)
white_estate_filter = white_trie_estate.pattern()
black_estate_filter = black_trie_estate.pattern()


chat_filter_money = filters.chat(CHATS_MONEY) & filters.text & key_money_filter
chat_filter_estate = filters.chat(CHATS_ESTATE) & filters.text & key_estate_filter

def searcher_main():

    print('* * * Starting... * * *')
    app = Client(name=APP_NAME, session_string=SESSION_STRING, in_memory=True)
    print('* * * STARTED SUCCESSFULLY ! * * *')

    @app.on_message(chat_filter_money)
    async def send_money(client, message):

        if re.search(white_money_filter, message.text, re.IGNORECASE):

            if re.search(black_money_filter, message.text, re.IGNORECASE):
                ic(message.text)
                pass
            else:
                message_for_bot = ''
                message_for_bot += f'{message.link}\n'
                message_for_bot += f'{message.text}\n'

                if message.from_user.username:
                    message_for_bot += f'Username: {message.from_user.username}\n'
                if message.from_user.first_name:
                    message_for_bot += f'First_name: {message.from_user.first_name}\n'
                if message.from_user.last_name:
                    message_for_bot += f'Last_name: {message.from_user.last_name}\n'
                if message.from_user.phone_number:
                    message_for_bot += f'Phone_number: {message.from_user.phone_number}\n'

                await send_money(message_for_bot)

    @app.on_message(chat_filter_estate)
    async def send_estate(client, message):

        if re.search(white_estate_filter, message.text, re.IGNORECASE):

            if re.search(black_estate_filter, message.text, re.IGNORECASE):
                ic(message.text)
                pass
            else:
                message_for_bot = ''
                message_for_bot += f'{message.link}\n'
                message_for_bot += f'{message.text}\n'

                if message.from_user.username:
                    message_for_bot += f'Username: {message.from_user.username}\n'
                if message.from_user.first_name:
                    message_for_bot += f'First_name: {message.from_user.first_name}\n'
                if message.from_user.last_name:
                    message_for_bot += f'Last_name: {message.from_user.last_name}\n'
                if message.from_user.phone_number:
                    message_for_bot += f'Phone_number: {message.from_user.phone_number}\n'

                await send_estate(message_for_bot)

    app.run()
    print('* * * Pyrogram App Closed * * *')


if __name__ == "__main__":
    searcher_main()
