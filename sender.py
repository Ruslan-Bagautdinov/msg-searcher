from bot_creator import bot
from searcher import GROUP_CHAT_ID


async def send_to_group(message_for_bot):

    await bot.send_message(int(GROUP_CHAT_ID),
                           message_for_bot
                           )
