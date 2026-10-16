import time

big_list = list(range(10_000_000))
big_set = set(big_list)

start = time.time()
9_999_999 in big_list
print("list:", time.time() - start)


start = time.time()
9_999_999 in big_set
print("set: " , time.time() - start)
