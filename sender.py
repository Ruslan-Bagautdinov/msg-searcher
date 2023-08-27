from bot_creator import bot, MONEY_CHAT_ID, ESTATE_CHAT_ID


async def send_money(message_for_bot):

    await bot.send_message(MONEY_CHAT_ID,
                           message_for_bot
                           )


async def send_estate(message_for_bot):

    await bot.send_message(ESTATE_CHAT_ID,
                           message_for_bot
                           )
