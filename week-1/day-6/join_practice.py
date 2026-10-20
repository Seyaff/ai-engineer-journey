print("+".join(["1", "2", "3"]))                  # 1
print("".join(["s", "i", "y", "a", "f"]))         # 2
print(" | ".join(["tea", "cake", "juice"]))       # 3
print("-".join(["solo"]))                          # 4
print("-".join([]))                                # 5
print("".join(sorted("cab")))                     # 6
print("".join(sorted("listen")) == "".join(sorted("silent")))   # 7
print(", ".join([str(n * 2) for n in range(3)]))  # 8