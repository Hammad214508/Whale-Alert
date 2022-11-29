# Whale-Alert
This script will enable you to track a bitcoin whale's activity by notifying you on telegram about any new transaction performed by their address on real time.

- It uses BotFather (A built-in Telegram bot that helps users create custom Telegram bots) to setup a bot to send messages.
- Runs every 10 minutes and checks whether a new transaction was added in the latest activity in order to send a notification on telegram.
- **Lite version**:
  - Uses BeautifulSoup to web-scrape information from BitInfoChart (website to retrieve a specific address' activity).
  - Might not be real time since it depends on when BitInfoChart updates their site.
  - Needs to store the last transaction's ID to check whether a new one was added.
- **Pro version**:
  - Uses Blockchain Info API to get real time data for the address' activity on the blockchain.
  - Uses Binance API to get the BTC price at that time.
  - Can easily be used as a cronjob since it doesn't require to store any data, it sends notification based on the timestamp of the transaction.
  - Will allow to track multiple addresses in a future release


## Setup telegram bot

### 1. Create A Telegram Bot Using Telegram’s BotFather

- Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots).
- Type /newbot to create a new bot.
- Give your bot a name & a username.
- Copy your new Telegram bot’s token into the script.

### 2. Getting your chat ID

- Send your Telegram bot a message (any random message)
- Run this Python script to find your chat ID;
```
import requests
TELEGRAM_TOKEN = "YOUR TELEGRAM BOT TOKEN"
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
print(requests.get(url).json())
```

This script calls the getUpdates function, which kinda checks for new messages. You can find your chat ID from the returned JSON.

Note: if you don’t send your Telegram bot a message, your results might be empty.

## Running the script
- Run `pip3 install -r requirements.txt` in order to install all the python dependencies required for running this project.
- Replace the `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` variables with your values gotten in the bot setup stage. Best practice is to add them as environment variables in your .zshrc or .bashrc and use `os.environ.get()` in the code to read them.
- Specify which bitcoin address you want to listen to in the `BITCOIN_ADDRESS` variable.
- Use `TIME_DELAY` to decide how often to check for an update, defaulted to every 10 minutes (Note: notification will only be sent if there was a new transaction).
- See the image below of an example notification:

[<img src="img/notification.png" width="250"/>](img/notification.png)


## TODO
- Allow tracking of multiple addresses.
- Add cronjob instructions so doens't need to run the application constantly.
- Turn this into a web application to make the user-experience better and make the script available to non-tech users.
