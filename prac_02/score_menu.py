import random

def generate_rectangle(length):
    width = random.randint(1, length)
    area = length * width
    return width, area

def get_valid_score():
    while True:
        score = int(input("Enter a valid score (0-100): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please try again.")

def print_result(score):
    print(f"The result is {score}")

def show_stars(score):
    print("*" * score)

def main():
    while True:
        print("\nMain Menu")
        print("---------")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            length = int(input("Enter the length: "))
            width, area = generate_rectangle(length)
            print(f"Width: {width}")
            print(f"Area: {area}")
        elif choice == "P":
            score = get_valid_score()
            print_result(score)
        elif choice == "S":
            score = get_valid_score()
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
