def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    
    reversed_text = ""
    for char in reversed(cleaned):
        reversed_text += char

    return cleaned == reversed_text


print(is_palindrome("Madam"))       
