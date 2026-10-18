stock = {"tea": 10, "cake": 0, "juice": 5}

print(stock["tea"])              # 1
print(stock.get("milk", -1))     # 2
print("cake" in stock)           # 3
print(5 in stock)                # 4
stock["cake"] = 7
print(stock["cake"])             # 5
stock["milk"] = 3
print(len(stock))                # 6
print(stock.get("juice"))        # 7
# print(stock["bread"])            # 8

# prints 10
# prints -1 because milk is not in stock
# prints true because cake is in stock 
# print false because there is no 5 key in dict 
# changes the cake price to 7 
# prints stock price of cake which is changed to 7
# adds milk and set price to 3
# prints 4 because we added milkk too
# prints the value of juice which is 5