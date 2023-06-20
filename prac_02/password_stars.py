MIN_PASSWORD_LENGTH = 8

while True:
    password = input("Enter your password: ")
    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password should be at least {MIN_PASSWORD_LENGTH} characters long. Please try again.")
    else:
        break

print("*" * len(password))


def main():
    MIN_PASSWORD_LENGTH = 8

    def print_password_asterisks(password):
        print("*" * len(password))

    while True:
        password = input("Enter your password: ")
        if len(password) < MIN_PASSWORD_LENGTH:
            get_password(MIN_PASSWORD_LENGTH)
        else:
            break

    print_password_asterisks(password)


def get_password(MIN_PASSWORD_LENGTH):
    print(f"Password should be at least {MIN_PASSWORD_LENGTH} characters long. Please try again.")


if __name__ == "__main__":
    main()
