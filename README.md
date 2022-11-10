# Whale-Alert
This script will enable to you track a crypto whale's activity by notifying you on telegram about any new transaction performed by their address.

- It uses BotFather (A built-in Telegram bot that helps users create custom Telegram bots) to setup a bot to send messages.
- BeautifulSoup to web-scrape information from BitInfoChart (website to retrieve a specific address' activity).
- Check whether a new bitcoin block got added into the latest activity in order to send a message. It will update every 5 minutes by default but can be changed.

## Setup telegram bot

### 1. Create A Telegram Bot Using Telegram’s BotFather

- Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots)
- Type /newbot to create a new bot
- Give your bot a name & a username
- Copy your new Telegram bot’s token into the script

### 2. Getting your chat ID

- Send your Telegram bot a message (any random message)
- Run this Python script to find your chat ID;
```
import requests
TOKEN = "YOUR TELEGRAM BOT TOKEN"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
```

This script calls the getUpdates function, which kinda checks for new messages. We can find our chat ID from the returned JSON (the one in red)

Note: if you don’t send your Telegram bot a message, your results might be empty.
- Copy and paste the chat ID into the script

## Running the script

- Replace the `TOKEN` and `chat_id` variables with your values gotten in the bot setup take
- Specify which bitcoin address you want to listen to in the `whale_address`
- Use `time_delay` to decide how often to check for an update (Note: notification will only be sent if there was a new block added)

## TODO
- Turn this into a web application to make the user-experience better and make the script available to non-tech users.
