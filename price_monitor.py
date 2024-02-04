import requests
import time
from threading import Thread

def fetch_crypto_price(crypto):
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    return response.json()[crypto]['usd']

def monitor_price(crypto, target_price, email):
    while True:
        current_price = fetch_crypto_price(crypto)
        print(f"Current price of {crypto}: ${current_price}")
        if current_price >= target_price:
            send_email(email, crypto, current_price)
            break
        time.sleep(60)  

def send_email(email, crypto, current_price):
    # Implement email sending logic
    print(f"Sending email to {email}: {crypto} has reached ${current_price}!")
