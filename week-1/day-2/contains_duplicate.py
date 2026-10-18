def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    # print(f"seen : {seen}")
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
            
            
    return



bro = has_duplicate([1,2,2,3,1])
print(bro)