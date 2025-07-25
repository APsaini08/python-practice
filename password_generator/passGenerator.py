import random
import string

def generate_password(length=12):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure at least one lowercase, one uppercase, one digit, and one special char
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)
    
    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)
    
    # Join to form the final password string
    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(16))
