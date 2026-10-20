def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        label = "".join(sorted(word))
        if label not in groups:
            groups[label] = []        
        groups[label].append(word)
        
    return list(groups.values())





result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)

assert result == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
assert group_anagrams([]) == []
assert group_anagrams(["a"]) == [["a"]]
assert group_anagrams(["ab", "ba", "ab"]) == [["ab", "ba", "ab"]]
print("All tests passed")