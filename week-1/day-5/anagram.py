def is_anagram(s ,t ):
    if len(s) != len(t):
        return False
    s_count = {}
    t_count = {}
    for s_letter , t_letter in zip(s,t):
        s_count[s_letter] = s_count.get(s_letter, 0) + 1
        t_count[t_letter] = t_count.get(t_letter, 0) + 1

    
    return s_count == t_count

result = is_anagram("book" , "koob")
print(result)


assert is_anagram("listen", "silent") == True
assert is_anagram("rat", "car") == False
assert is_anagram("aab", "abb") == False
assert is_anagram("a", "ab") == False
assert is_anagram("", "") == True
print("All tests passed")