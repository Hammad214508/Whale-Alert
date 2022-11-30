import os
import requests
import time
from datetime import datetime, timedelta

def send_message(message):
    url = f"{TELEGRAM_BOT_API}{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    requests.get(url)

def get_transaction_summary():
    url = f"{BLOCKCHAIN_INFO_API}{BITCOIN_ADDRESS}?&limit=1"
    response = requests.get(url).json()
    transaction = response["txs"][0]
    transaction_time = datetime.fromtimestamp(transaction["time"])
    transaction_result = '{0:.8f}'.format(transaction["result"]/100000000)
    return (transaction_time, transaction_result)

def get_bitcoin_price():
    response = requests.get(BINANCE_API).json()
    return float(response['price'])

BLOCKCHAIN_INFO_API = "https://blockchain.info/rawaddr/"
BINANCE_API = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
TELEGRAM_BOT_API = "https://api.telegram.org/bot"
TELEGRAM_TOKEN =  os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
BITCOIN_ADDRESS = "1LQoWist8KkaUXSPKZHNvEyfrEkPHzSsCd"
TIME_DELAY = 10 * 60 # every 10 minutes

while(True):
    current_time = datetime.now()
    last_run = current_time - timedelta(seconds=TIME_DELAY)
    transaction_time, transaction_result = get_transaction_summary()
    if (last_run <= transaction_time <= current_time):
        bitcoin_price = get_bitcoin_price()
        transaction_value = round(abs(float(transaction_result)) * bitcoin_price, 2)
        transaction_summary = "{} BTC (${}) at ${}".format(transaction_result, transaction_value, bitcoin_price)
        print(transaction_summary)
        send_message(transaction_summary)
    time.sleep(TIME_DELAY)
