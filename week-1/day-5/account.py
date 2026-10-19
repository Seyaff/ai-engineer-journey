class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("bad amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance: 
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance


acc = Account("ali")
acc.deposit(500)
assert acc.get_balance() == 500

assert acc.withdraw(200) == True
assert acc.get_balance() == 300

assert acc.withdraw(1000) == False
assert acc.get_balance() == 300

assert acc.withdraw(300) == True 
assert acc.get_balance() == 0

other = Account("sara")
assert other.get_balance() == 0
print("All tests passed")


acc = Account("ali")
acc.deposit(500)
assert acc.get_balance() == 500

try:
    acc.deposit(-100)
    assert False, "should have raised"
except ValueError:
    pass
assert acc.get_balance() == 500

try:
    acc.deposit(0)
    assert False, "should have raised"
except ValueError:
    pass
print("Account tests passed")