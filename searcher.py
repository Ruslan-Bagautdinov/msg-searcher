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








# # #
# from telethon import TelegramClient, sync
# from os import getenv

# api_id = 29162559
# api_hash = '0a58fc2814ed366c9dc731d682663949'
#
#
# SERVER = getenv('SERVER')
#
# if SERVER:
#     API_ID = int(getenv('API_ID'))
#     API_HASH = getenv('API_HASH')
#     USERNAME = getenv('USERNAME')
#     PHONE_NUMBER = getenv('PHONE_NUMBER')
#     STRING = getenv('STRING')
#
# else:
#     from config import API_ID, API_HASH, USERNAME, PHONE_NUMBER, STRING
#
#     API_ID = int(API_ID)
#     API_HASH = API_HASH
#     USERNAME = USERNAME
#     PHONE_NUMBER = PHONE_NUMBER
#     STRING = STRING
#
# PATTERN = pattern = re.compile(r'обмен|наличн|помен|рубл|курс|перевод', re.IGNORECASE)
#
#
#
# chats = ('+jzWUJ4kYorQ4YWI6',
#          'AlanyaVse',
#          'alanya_chat_2',
#          'alaniya_chat_kg',
#          'alanyachat_cho',
#          'alanya_bestchat',
#          'alanyamahmutlargazipasa',
#          'alanya_2022',
#          'alaniyalife',
#          'alanyaru',
#          'alanya_forum',
#          'alanya_profi',
#          'alanya_top',
#          'chatalanya_turkey',
#          'globe_alaniya_chat',
#          'mahmutlarrussia',
#          'mahmutlarru_chat',
#          'mahmutlarru',
#          'mamochkanamore',
#          'mahmutlar_online',
#          'Vmeste_Alanya'
#          )
#
# client = TelegramClient('ruslan', api_id, api_hash)
# client.start()
#
#
# client.run_until_disconnected()












# import re
#
# from icecream import ic
#
# from telethon.sync import TelegramClient, events
# from telethon.sessions import StringSession
#
# from os import getenv
#
# from time import sleep
#
# SERVER = getenv('SERVER')
#
# if SERVER:
#     API_ID = int(getenv('API_ID'))
#     API_HASH = getenv('API_HASH')
#     USERNAME = getenv('USERNAME')
#     PHONE_NUMBER = getenv('PHONE_NUMBER')
#     STRING = getenv('STRING')
#
# else:
#     from config import API_ID, API_HASH, USERNAME, PHONE_NUMBER, STRING
#
#     API_ID = int(API_ID)
#     API_HASH = API_HASH
#     USERNAME = USERNAME
#     PHONE_NUMBER = PHONE_NUMBER
#     STRING = STRING
#
# PATTERN = pattern = re.compile(r'обмен|наличн|помен|рубл|курс|перевод', re.IGNORECASE)
#
#
# async def main():
#
#     await client.connect()
#
#     chats = ('+jzWUJ4kYorQ4YWI6',
#              'alanya_bestchat',
#              'alanyamahmutlargazipasa',
#              'mahmutlarrussia',
#              'mahmutlarru_chat',
#              'alanya_2022',
#              'alaniyalife',
#              'alanyaru',
#              'alanya_forum',
#              'chatalanya_turkey',
#              'mamochkanamore',
#              'alanya_profi',
#              'mahmutlar_online',
#              'Vmeste_Alanya',
#              'mahmutlarru_chat'
#              )
#
#     @client.on(events.NewMessage(chats=chats))
#     async def normal_handler(event):
#         new_message = event.message.to_dict()['message']
#
#         match = PATTERN.search(new_message)
#         if match:
#
#             sleep(1)
#
#             sender = await event.get_sender()
#
#             ic(sender)
#
#             sender_name = 'Отправитель:'
#
#             if sender.first_name:
#                 sender_name += f' {sender.first_name} '
#
#             if sender.last_name:
#                 sender_name += f' {sender.last_name} '
#
#             forwarded_message = f'{sender_name}: {event.message.to_dict()["message"]}'
#
#             await client.send_message('Alexandra_Exchange', forwarded_message)
#
#             sleep(2)
#
#             chat_id = event.message.to_id.channel_id
#
#             messages = await client.get_messages(chat_id, ids=[event.message.id])
#
#             sleep(1)
#
#             message_link = f'https://t.me/c/{messages[0].chat.id}/{messages[0].id}'
#
#             ic(message_link)
#
#             await client.send_message('Alexandra_Exchange', message_link)
#
#             sleep(2)
#
#     await client.run_until_disconnected()
#
#
# with TelegramClient(StringSession(STRING),
#                     API_ID,
#                     API_HASH,
#                     system_version="4.16.30-vxCUSTOM",
#                     app_version="1.28.5",
#                     device_model="AMD64",
#                     lang_code="ru"
#                     ) as client:
#     client.loop.run_until_complete(main())

