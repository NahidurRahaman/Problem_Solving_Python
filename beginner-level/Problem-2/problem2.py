def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count


input_sentence = "Data Science is awesome"
print(count_vowels(input_sentence))  
