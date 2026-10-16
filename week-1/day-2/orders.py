def order_summary(orders: list[dict]) -> dict:
    total = sum(o["price"] * o["qty"] for o in orders)
    
    by_item = {}
    for o in orders :
        by_item[o["item"]] = by_item.get(o["item"] , 0) + o["qty"]
    if len(orders)==0:
        biggest = None
    else:
        biggest = max(orders , key=lambda x: x["price"] * x["qty"])["id"]
       
    
    

    return {"total": total , "by_item" : by_item , "biggest" : biggest}


orders = [
    {"id": 1, "item": "zinger", "qty": 2, "price": 450},
    {"id": 2, "item": "fries",  "qty": 1, "price": 200},
    {"id": 3, "item": "zinger", "qty": 1, "price": 450},
]

orders2 = [
    {"id": 1, "item": "fries",   "qty": 5, "price": 100},   # 5 × 100  = 500
    {"id": 2, "item": "biryani", "qty": 1, "price": 1200},  # 1 × 1200 = 1200 ← biggest
]
print(order_summary(orders2)["biggest"])
print(order_summary(orders))     # should print {'total': 1550}
print(order_summary([]))         # should print {'total': 0}

assert order_summary(orders2)["biggest"] == 2