def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


print(longest_word("Machine learning is fascinating"))  
