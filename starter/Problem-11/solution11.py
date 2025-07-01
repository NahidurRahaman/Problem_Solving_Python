rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

char_count = {}
for char in rhyme:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

mx = 0
mx_char = ''
for char, count in char_count.items():
    if count > mx and char != ' ':
        mx = count
        mx_char = char


print(f"The most frequent character is '{mx_char}' with {mx} occurrences.")
print(char_count)