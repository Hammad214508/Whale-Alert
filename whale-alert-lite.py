import os
import time
import requests
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

def webscrap_latest_transaction():
    website = get_website()
    tr = website.find(id="table_maina").find_next('tbody').find_next('tr')
    td_list = tr.find_all("td")
    block_number = td_list[0].find_next('a').get_text()
    amount = td_list[1].find_next('span').get_text()
    price = td_list[4].get_text().split("@",1)[1]
    return (block_number, amount + " at" + price)

TELEGRAM_TOKEN =  os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
BIT_INFO_CHARTS = "https://bitinfocharts.com/bitcoin/address/"
BITCOIN_ADDRESS = "1LQoWist8KkaUXSPKZHNvEyfrEkPHzSsCd"
TIME_DELAY = 10 * 60 # every 10 minutes

current_block = webscrap_latest_transaction()[0]+"1"

while(True):
    latest_block, transaction = webscrap_latest_transaction()
    if (current_block != latest_block):
        current_block = latest_block
        print(transaction)
        send_message(transaction)
    time.sleep(TIME_DELAY)
