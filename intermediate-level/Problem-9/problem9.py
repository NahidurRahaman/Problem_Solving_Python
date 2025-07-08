def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return False, "Password must include at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return False, "Password must include at least one number."
    
    special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    if not any(char in special_chars for char in password):
        return False, "Password must include at least one special character."
    
    return True, "Password is valid."


password = "MyStrongPass1!"
valid, message = is_valid_password(password)
print(message)
