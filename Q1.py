import re

def check_password_strength(password: str) -> bool:
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not re.search(r"\d", password):
        print("Password must contain at least one digit (0-9).")
        return False
    if not re.search(r"[@$!%*?&]", password):
        print("Password must contain at least one special character (@, $, !, %, *, ?, &).")
        return False
    
    return True

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    if check_password_strength(password):
        print("Strong password!")
    else:
        print("Please choose a stronger password.")