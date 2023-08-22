from pyrogram import Client, filters
import re

from icecream import ic

# own imports
from bot_creator import APP_NAME, SESSION_STRING

from sender import send_to_group

from key_words import CHATS, KEY_WORDS, BLACK_LIST, WHITE_LIST
from trie import Trie


key_words_filter = filters.regex(f"({'|'.join(KEY_WORDS)})", flags=re.IGNORECASE)

white_trie = Trie()
black_trie = Trie()
for word in sorted(WHITE_LIST):
    white_trie.add(word)
for word in sorted(BLACK_LIST):
    black_trie.add(word)
white_list_filter = white_trie.pattern()
black_list_filter = black_trie.pattern()

chat_filter = filters.chat(CHATS) & filters.text & key_words_filter


def searcher_main():

    print('* * * Starting... * * *')
    app = Client(name=APP_NAME, session_string=SESSION_STRING, in_memory=True)
    print('* * * STARTED SUCCESSFULLY ! * * *')

    @app.on_message(chat_filter)
    async def send_link(client, message):

        if re.search(white_list_filter, message.text, re.IGNORECASE):

            if re.search(black_list_filter, message.text, re.IGNORECASE):
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

                await send_to_group(message_for_bot)

    app.run()
    print('* * * Pyrogram App Closed * * *')


if __name__ == "__main__":
    searcher_main()
