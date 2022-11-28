import requests
import pandas as pd

import requests

users_info = {
    "Alexia": {"balance (EUR)":10000, "portfolio":{}},
    "Christopher": {"balance (EUR)":10000, "portfolio":{}},
    "Michelle": {"balance (EUR)":10000, "portfolio":{}}
}

fx_rates = {
    "USD/EUR": 0.96,
    "DKK/EUR": 0.13,
    "GBP/EUR": 1.16
}

def buy_stock():
    stock = input("which stock? ")
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock + "&interval=5min&outputsize=full&apikey=KOA81QCGI4HZS0CJ")
    raw_data = response.json()
    stock_price = int(float(raw_data['Time Series (5min)']['2022-11-23 17:40:00']['4. close']))
    quant = int(input('Enter buying quantity: '))
    response_cur = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + stock + "&apikey=KOA81QCGI4HZS0CJ")
    raw_data_cur = response_cur.json()
    stock_cur = raw_data_cur["bestMatches"][0]["8. currency"]

    # remember that these stock are not owned by the user
    print(stock_price*quant)
    if stock in users_info[current_user]['portfolio']:
        users_info[current_user]['portfolio'][stock] += quant
    else:
        users_info[current_user]['portfolio'][stock] = quant

    if stock_cur == "USD":
        eur_stock_price = fx_rates["USD/EUR"] * stock_price
        users_info[current_user]['balance (EUR)'] -= eur_stock_price * quant
    elif stock_cur == "DKK":
        dkk_stock_price = fx_rates["DKK/EUR"] * stock_price
        users_info[current_user]['balance (EUR)'] -= dkk_stock_price * quant
    elif stock_cur == "GBP":
        gbp_stock_price = fx_rates["DKK/EUR"] * stock_price
        users_info[current_user]['balance (EUR)'] -= gbp_stock_price * quant
    else:
        print("currency not found")

def sell_stock():
    stock = input("which stock? ")
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock + "&interval=5min&outputsize=full&apikey=KOA81QCGI4HZS0CJ")
    raw_data = response.json()
    stock_price = int(float(raw_data['Time Series (5min)']['2022-11-23 17:40:00']['4. close']))
    print(stock_price)
    quant = int(input('Enter selling quantity: '))
    # remember that these stock are not owned by the user
    users_info[current_user]['portfolio'][stock] -= quant
    response_cur = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + stock + "&apikey=KOA81QCGI4HZS0CJ")
    raw_data_cur = response_cur.json()
    stock_cur = raw_data_cur["bestMatches"][0]["8. currency"]
    print(stock_cur)

    if stock_cur == "USD":
        eur_stock_price = fx_rates["USD/EUR"]*stock_price
        users_info[current_user]['balance (EUR)'] += eur_stock_price * quant
    elif stock_cur == "DKK":
        dkk_stock_price = fx_rates["DKK/EUR"] * stock_price
        users_info[current_user]['balance (EUR)'] += dkk_stock_price * quant
    elif stock_cur == "GBP":
        gbp_stock_price = fx_rates["DKK/EUR"] * stock_price
        users_info[current_user]['balance (EUR)'] += gbp_stock_price * quant
    else:
        print("currency not found")


name = input("What is your name?")
current_user = name
while True:
    choice = input("What do you want to do? (buy/sell/new_user/quit) ")
    if choice == "buy":
        buy_stock()
    elif choice == "sell":
        sell_stock()
    elif choice == "new_user":
        name = input("What is your name?")
        current_user = name
    elif choice == "quit":
        break
    print(users_info)

import requests
keyword = input("Give keyword (symbol/name)")
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + keyword + "&apikey=KOA81QCGI4HZS0CJ"
r = requests.get(url)
data = r.json()

#print(data)

print(data["bestMatches"])
for i in data["bestMatches"]:
    print(data["bestMatches"][])
#print(data)
#'FRD'
def fund():
    my_list = list(cr)
    symbol = input("Give the symbol: ")
 #   for symbol in my_list[0]:
    print(f"The information is: {my_list[0:6]}")

fund()
print(my_list[0][0])


