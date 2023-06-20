MIN_PASSWORD_LENGTH = 8

while True:
    password = input("Enter your password: ")
    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password should be at least {MIN_PASSWORD_LENGTH} characters long. Please try again.")
    else:
        break

print("*" * len(password))