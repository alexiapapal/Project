import requests
import pandas as pd



response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")



# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

raw_data.keys()

# Let's look at the first key/value.
# This is just some descriptive information
raw_data['Meta Data']

# The other key/value pair is the actual time series.
# This is a dict as well
time_series = raw_data['Time Series (5min)']
print(type(time_series))

print(len(time_series))

# Let's take the first few keys
first_ten_keys = list(time_series.keys())[:10]

# And see the corresponding values
first_ten_items = [f"{key}: {time_series[key]}" for key in first_ten_keys ]
print("\n".join(first_ten_items))


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

#df[['open', 'high', 'low', 'close']].plot()

#### Resampling

# Let's take last value of the close column for every business day
close_per_day = df.close.resample('B').last()

import matplotlib.pyplot as plt
#close_per_day.plt.show()


price = df['close'][2]
owned_stocks = {'TSLA': 0, 'TWTR':0, 'NFLX':0}

stockinfo = {"stock_name": '', "quantity": 0, "money": 0}

userinfo = {'total_balance': 1000}
def buy_stock(price, stock):
    choice = int(input('Enter buying quantity: '))
    cost = choice * price
    stockinfo['quantity'] += choice
    stockinfo['money'] += cost
    stockinfo['stock_name'] = stock
    userinfo['total_balance'] -= cost

buy_stock(price, 'TSLA')
print(stockinfo, userinfo)

def sell_stock(price, stock):
    choice = int(input('Enter selling quantity: '))
    cost = choice * price
    stockinfo['quantity'] -= choice
    stockinfo['money'] -= cost
    stockinfo['stock_name'] = stock
    userinfo['total_balance'] += cost


sell_stock(price, 'TSLA')
print(stockinfo, userinfo)

def limit_stock(price, stock, threshold):
    if price <= threshold:
        buy_stock(price, stock)
    else:
        print("It's too expensive girl, don't buy...sell!")
        sell_stock(price,stock)


limit_stock(price, 'TSLA', 100)
print(stockinfo, userinfo)