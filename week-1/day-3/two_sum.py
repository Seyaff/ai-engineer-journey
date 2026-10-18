def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}            
    for i, n in enumerate(nums):
        print(i , n)
        need = target - n
        if need in seen:        # ❌ fix 2
            return [seen[need], i]
        seen[n] = i
    return []


bro = two_sum([2,7,4,6],9)
print(bro)