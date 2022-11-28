import requests

# Use FX rate
fx_rates = {
    "USD/EUR": 0.96,
    "DKK/EUR": 0.13,
    "GBP/EUR": 1.16
}
#
# input:
# users_info: dictionary consisting of mulitple users information
# current_user: string with a user name from the users info


def buy_stock(users_info, current_user):
    keyword = input("Give keyword (symbol/name)")
    url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + keyword + "&apikey=KOA81QCGI4HZS0CJ"
    r = requests.get(url)
    data = r.json()
    for i in data["bestMatches"]:
        symbol = (i["1. symbol"])
        name = (i["2. name"])
        print(symbol, name)

    stock = input("which ticker?")
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock + "&interval=5min&outputsize=full&apikey=KOA81QCGI4HZS0CJ")
    raw_data = response.json()
    stock_price = int(float(raw_data['Time Series (5min)']['2022-11-23 17:40:00']['4. close']))

    quant = int(input('Enter buying quantity: '))
    response_cur = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + stock + "&apikey=KOA81QCGI4HZS0CJ")
    raw_data_cur = response_cur.json()
    stock_cur = raw_data_cur["bestMatches"][0]["8. currency"]


    # Do not buy stock if the stock*quant is higher than our portfolio
    if (stock_price*quant) > users_info[current_user]['balance (EUR)']:
        print("You don't have enough money")
    else:
        # remember that these stock are not owned by the user
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

def sell_stock(users_info, current_user):
    keyword = input("Give keyword (symbol/name)")
    url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + keyword + "&apikey=KOA81QCGI4HZS0CJ"
    r = requests.get(url)
    data = r.json()
    for i in data["bestMatches"]:
        symbol = (i["1. symbol"])
        name = (i["2. name"])
        print(symbol, name)

    stock = input("which ticker? ")
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock + "&interval=5min&outputsize=full&apikey=KOA81QCGI4HZS0CJ")
    raw_data = response.json()
    stock_price = int(float(raw_data['Time Series (5min)']['2022-11-23 17:40:00']['4. close']))
    quant = int(input('Enter selling quantity: '))
    # remember that these stock are not owned by the user

    response_cur = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + stock + "&apikey=KOA81QCGI4HZS0CJ")
    raw_data_cur = response_cur.json()
    stock_cur = raw_data_cur["bestMatches"][0]["8. currency"]

    if (stock in users_info[current_user]['portfolio']) and (users_info[current_user]['portfolio'][stock] >= quant):
        users_info[current_user]['portfolio'][stock] -= quant
        if stock_cur == "USD":
            eur_stock_price = fx_rates["USD/EUR"] * stock_price
            users_info[current_user]['balance (EUR)'] += eur_stock_price * quant
        elif stock_cur == "DKK":
            dkk_stock_price = fx_rates["DKK/EUR"] * stock_price
            users_info[current_user]['balance (EUR)'] += dkk_stock_price * quant
        elif stock_cur == "GBP":
            gbp_stock_price = fx_rates["DKK/EUR"] * stock_price
            users_info[current_user]['balance (EUR)'] += gbp_stock_price * quant
        else:
            print("currency not found")
    else:
        print("You don't own enough stocks!")