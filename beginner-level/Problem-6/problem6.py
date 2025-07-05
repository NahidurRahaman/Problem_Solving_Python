def capitalize_words(text):
    words = text.split()
    capitalized = []
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
            capitalized.append(capitalized_word)
    return ' '.join(capitalized)

input_text = "python for web developers"
output = capitalize_words(input_text)
print(output)
