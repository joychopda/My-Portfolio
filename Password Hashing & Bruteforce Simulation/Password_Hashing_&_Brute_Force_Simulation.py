import bcrypt

# Hash password
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

# Check password
def check_password(stored_password: bytes, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode(), stored_password)

# Brute-force example
def brute_force(password_hash: bytes, password_list: list) -> str:
    for password in password_list:
        if check_password(password_hash, password):
            return f"Password found: {password}"
    return "Password not found in dictionary"

# Test
password_to_hash = "securePassword!"
hashed_password = hash_password(password_to_hash)
print("Stored hash:", hashed_password)

# Simulate validation and brute-force attack
password_attempt = "securePassword!"
print("Password validation:", check_password(hashed_password, password_attempt))

# Simulate a brute-force attempt
password_list = ['password123', '123456', 'admin', 'letmein', 'welcome']
print(brute_force(hashed_password, password_list))