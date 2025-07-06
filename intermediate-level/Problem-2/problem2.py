from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())


print(group_anagrams(["bat", "tab", "cat", "act"]))  
