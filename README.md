# Telegram Message Filter Bot

This project is a Telegram bot that monitors specific chats for messages related to money exchange and apartment rentals. It uses Pyrogram for reading messages and Aiogram for sending messages based on predefined filters.

## Features

- Monitors multiple chats for messages.
- Filters messages based on keywords, white lists, and black lists.
- Sends filtered messages to specified chats.
- Uses a Trie data structure for efficient pattern matching.

## Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/telegram-message-filter-bot.git
cd telegram-message-filter-bot
```

2. Install the required packages:
```sh
pip install -r requirements.txt
```

3. Set up your environment variables by creating a .env file in the root directory with the following content:
```dotenv
APP_NAME=your_app_name
API_ID=your_api_id
API_HASH=your_api_hash
USERNAME=your_username
PHONE_NUMBER=your_phone_number
BOT_NAME=your_bot_name
BOT_TOKEN=your_bot_token
SESSION_STRING=your_session_string
MONEY_CHAT_ID=your_money_chat_id
ESTATE_CHAT_ID=your_estate_chat_id
```

4. Run the bot:
```sh
python searcher.py
```

### Configuration
- APP_NAME: The name of your Pyrogram app.

- API_ID: Your Telegram API ID.

- API_HASH: Your Telegram API hash.

- USERNAME: Your Telegram username.

- PHONE_NUMBER: Your Telegram phone number.

- BOT_NAME: The name of your Aiogram bot.

- BOT_TOKEN: The token for your Aiogram bot.

- SESSION_STRING: The session string for your Pyrogram app.

- MONEY_CHAT_ID: The chat ID where money-related messages will be sent.

- ESTATE_CHAT_ID: The chat ID where estate-related messages will be sent.

### Usage
Ensure that the Pyrogram account is added to the chats you want to monitor.

The bot will automatically start monitoring the specified chats and send filtered messages to the designated chats.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is unlicensed and is free to use, modify, and distribute without any restrictions.