import requests
import time
from bs4 import BeautifulSoup

def send_message(message):
    TOKEN = "Your token"
    chat_id = "Your chat id"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def get_latest_block_price():
    bitinfocharts="https://bitinfocharts.com/bitcoin/address/"
    url = bitinfocharts + whale_address
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    tr = soup.find(id="table_maina").find_next('tbody').find_next('tr')
    td_list = tr.find_all("td")
    block_number = td_list[0].find_next('a').get_text()
    amount = td_list[1].find_next('span').get_text()
    price = td_list[4].get_text().split("@",1)[1]
    return (block_number, amount + " at" + price)

whale_address = "1LQoWist8KkaUXSPKZHNvEyfrEkPHzSsCd"
time_delay = 300 # every 5 minutes
current_block = get_latest_block_price()[0]

while(True):
    latest_block, transaction = get_latest_block_price()
    if (current_block != latest_block):
        current_block = latest_block
        send_message(transaction)
    time.sleep(time_delay)
    
