import os
import requests
import time
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    requests.get(url)

def get_website():
    url = BIT_INFO_CHARTS + BITCOIN_ADDRESS
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, "html.parser")

def get_transaction_summary(transaction_data):
    amount = transaction_data[1].find_next('span').get_text()
    price = transaction_data[4].get_text().split("@",1)[1]
    return (amount + " at" + price)

def webscrap_latest_transaction():
    website = get_website()
    first_row = website.find(id="table_maina").find_next('tbody').find_next('tr')
    row_entries = first_row.find_all("td")
    datetime_str = row_entries[1].get_text()
    transaction_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %Z')
    transaction_summary = get_transaction_summary(row_entries)
    return transaction_time, transaction_summary

TELEGRAM_TOKEN =  os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
BIT_INFO_CHARTS="https://bitinfocharts.com/bitcoin/address/"
BITCOIN_ADDRESS = "1LQoWist8KkaUXSPKZHNvEyfrEkPHzSsCd"
TIME_DELAY = 10*60 # every 10 minutes

while(True):
    current_time = datetime.now()
    last_run = current_time - timedelta(seconds=TIME_DELAY)
    transaction_time, transaction_summary = webscrap_latest_transaction()
    if (last_run <= transaction_time <= current_time):
        print(transaction_summary)
        send_message(transaction_summary)
    time.sleep(TIME_DELAY)
