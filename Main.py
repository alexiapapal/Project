import requests
import pandas as pd


import requests


stock = "MSFT"
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+stock+"&interval=5min&outputsize=full&apikey=demo")
print(response)

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

#raw_data.keys()
# Let's look at the first key/value.
# This is just some descriptive information
# raw_data['Meta Data']

# The other key/value pair is the actual time series.
# This is a dict as well
# time_series = raw_data['Time Series (5min)']
# print(type(time_series))
#
# print(len(time_series))
#
# # Let's take the first few keys
# first_ten_keys = list(time_series.keys())[:10]
#
# # And see the corresponding values
# first_ten_items = [f"{key}: {time_series[key]}" for key in first_ten_keys ]
# print("\n".join(first_ten_items))


#########################################
########## CREATING DATAFRAME ###########
#########################################


data = raw_data['Time Series (5min)']
df = pd.DataFrame(data).T.apply(pd.to_numeric)
df.info()
df.head()
print(df)

# Next we parse the index to create a datetimeindex
df.index = pd.DatetimeIndex(df.index)

# Let's fix the column names by chopping off the first 3 characters
df.rename(columns=lambda s: s[3:], inplace=True)

df.info()

df.head()

df[['open', 'high', 'low', 'close']].plot()

#### Resampling

# Let's take last value of the close column for every business day
close_per_day = df.close.resample('B').last()

import matplotlib.pyplot as plt
#close_per_day.plt.show()


stock_price = {
    "MSFT" : 10,
    "APPLE" : 15,
    "TSLA" : 5,
    "BITCOIN" : 100
}


users_info = {
    "Alexia": {"balance":10000, "portfolio":{}},
    "Chrisopher": {"balance":10000, "portfolio":{}},
    "Michelle": {"balance":10000, "portfolio":{}}
}



def buy_stock():
    stock = input("which stock? ")
    if stock in stock_price:
        price = stock_price[stock]
    else:
        print("This does not exists")
    quant = int(input('Enter buying quantity: '))
    # remember that these stock are not owned by the user
    print(price*quant)

    users_info[current_user]['portfolio'][stock] = quant
    users_info[current_user]['balance'] -= price * quant

def sell_stock():
    stock = input("which stock? ")
    if stock in stock_price:
        price = stock_price[stock]
    else:
        print("This does not exists")
    quant = int(input('Enter buying quantity: '))
    # remember that these stock are not owned by the user
    print(price*quant)

    users_info[current_user]['portfolio'][stock] -= quant
    users_info[current_user]['balance'] += price * quant




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







# buy_stock(price, 'TSLA')
# print(stockinfo, userinfo)





#
# sell_stock(price, 'TSLA')
# print(stockinfo, userinfo)
#
#
#
#
# limit_stock(price, 'TSLA', 100)
# print(stockinfo, userinfo)
#
#
#
# stop_order(price, 'TSLA', price)
# print(stockinfo,userinfo)

