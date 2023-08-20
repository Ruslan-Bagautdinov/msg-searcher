from pyrogram import Client, filters
import re

from icecream import ic

# own imports
from config import APP_NAME, SESSION_STRING
from sender import send_to_group

chats = ['test_Alexandra_Exchange',
         '+jzWUJ4kYorQ4YWI6',
         'AlanyaVse',
         'alanya_chat_2',
         'alaniya_chat_kg',
         'alanyachat_cho',
         'alanya_bestchat',
         'alanyamahmutlargazipasa',
         'alanya_2022',
         'alaniyalife',
         'alanyaru',
         'alanya_forum',
         'alanya_profi',
         'alanya_top',
         'chatalanya_turkey',
         'globe_alaniya_chat',
         'mahmutlarrussia',
         'mahmutlarru_chat',
         'mahmutlarru',
         'mamochkanamore',
         'mahmutlar_online',
         'Vmeste_Alanya'
         ]

key_words = ['обмен', 'наличн', 'помен', 'рубл', 'курс', 'перевод', 'валют']

black_list = ['Добро пожаловать в наш чат',
              'в курсе',
              'конкурс'
              'переводчик',
              'устный перевод',
              'заработ',
              'заходите на канал',
              'Капуста']

key_words_filter = filters.regex(f"({'|'.join(key_words)})", flags=re.IGNORECASE)
black_list_filter = f"({'|'.join(black_list)})"

chat_filter = filters.chat(chats) & filters.text & key_words_filter


def searcher_main():

    print('Starting...')
    app = Client(name=APP_NAME, session_string=SESSION_STRING, in_memory=True)
    print('* STARTED SUCCESSFULLY *')

    @app.on_message(chat_filter)
    async def send_link(client, message):

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
    print('... Pyrogram App Closed ...')


if __name__ == "__main__":
    searcher_main()








