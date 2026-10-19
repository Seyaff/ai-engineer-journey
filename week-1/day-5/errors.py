def parse_price(text):
    try:
        price = int(text)       # only this line inside try
    except ValueError:
        return None
    if price < 0:               # outside try: nothing catches this
        raise ValueError("negative price")
    return price
    
    
    
    
    
bro = parse_price("siyaf")
print(bro)

assert parse_price("450") == 450
assert parse_price("abc") is None
assert parse_price("") is None
try:
    parse_price("-50")
    assert False, "should have raised"
except ValueError:
    pass
print("All tests passed")