def two_sum(nums : list[int] , target: int) -> list[int]:
    seen = {2:0}
    for i , n in enumerate(nums):
        need = target - n
        if n in seen:
            return [seen[need] , i]
        seen[n] = i
        
    return []
        
        
print(two_sum([2, 7, 11, 15], 9))



# bro = {2:0,1:1,3:4}
# print(bro[2])