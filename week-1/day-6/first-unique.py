def first_unique(word):
    
    letters_count = {}
    for letter in word:
        letters_count[letter] = letters_count.get(letter , 0) + 1
    
    for i , letter in enumerate(word):
        if letters_count[letter] == 1:
            return i  
    
    return -1
    
    

assert first_unique("leetcode") == 0
assert first_unique("loveleetcode") == 2
assert first_unique("swiss") == 1
assert first_unique("aabb") == -1
assert first_unique("") == -1
assert first_unique("z") == 0
print("All tests passed")