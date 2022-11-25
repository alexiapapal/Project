
def limit_stock(price, stock, threshold):
    if price <= threshold:
        buy_stock(price, stock)
    else:
        print("It's too expensive girl, don't buy...sell!")
        sell_stock(price,stock)

def stop_order(price, stock, stop_threshold):
     if price == stop_threshold:
        print("You can buy or sell the stocks.")
        user_input = input("Please give a buy or sell argument: ")
        if user_input == "buy":
            buy_stock(price, stock)
        else:
            sell_stock(price, stock)
    else:
        print("The stock threshold has not been reached yet.")