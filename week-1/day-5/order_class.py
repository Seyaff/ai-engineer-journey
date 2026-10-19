class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, name, price, qty=1):
        order_dict = {"name": name, "price": price, "qty": qty}
        self.items.append(order_dict)

    def total(self):
        total_sum = sum(n["price"] * n["qty"] for n in self.items)
        return total_sum

    def item_count(self):
        sum_of_qty = sum(n["qty"] for n in self.items)
        return sum_of_qty

    def remove_item(self, item_name):
        before = len(self.items)
        self.items = [n for n in self.items if n["name"] != item_name]
        return len(self.items) < before

    def __repr__(self):

        return f"Order({self.customer}, {self.item_count()} items, Rs {self.total()})"


o = Order("ali")
o.add_item("zinger", 450, 2)
o.add_item("fries", 200)


assert o.total() == 1100
assert o.item_count() == 3
assert repr(o) == "Order(ali, 3 items, Rs 1100)"

o2 = Order("sara")
assert o2.total() == 0
assert o2.item_count() == 0
assert o.total() == 1100
o.remove_item("fries")
print(o)


print("All tests passed")


o3 = Order("bilal")
o3.add_item("zinger", 450, 2)
o3.add_item("cola", 100)
assert o3.remove_item("cola") == True
assert o3.total() == 900
assert o3.remove_item("pizza") == False
assert o3.total() == 900
print("remove_item tests passed")