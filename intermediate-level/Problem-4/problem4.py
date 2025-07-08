import re

def is_valid_email(email: str):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

print(is_valid_email("test@domain.com"))    
print(is_valid_email("hello.world@site.co")) 
print(is_valid_email("invalid@com"))         
print(is_valid_email("noatsign.com"))        
print(is_valid_email("a@b"))                 
