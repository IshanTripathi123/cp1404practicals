name = input("Enter name: ")


def display_menu():
    print("Menu:")
    print("H - Say hello")
    print("G - Say goodbye")
    print("Q - Quit")


display_menu()
choice = input("Enter choice: ")

while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
