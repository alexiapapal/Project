from Functions import *

# Get user info
users_info = {
    "Alexia": {"balance (EUR)":10000, "portfolio":{}},
    "Christopher": {"balance (EUR)":10000, "portfolio":{}},
    "Michelle": {"balance (EUR)":10000, "portfolio":{}}
}

name = input("What is your name?")
current_user = name
while True:
    choice = input("What do you want to do? (buy/sell/new_user/quit) ")
    if choice == "buy":
        buy_stock(users_info, current_user)
    elif choice == "sell":
        sell_stock(users_info, current_user)
    elif choice == "new_user":
        name = input("What is your name?")
        current_user = name
    elif choice == "quit":
        break
    print(users_info)





