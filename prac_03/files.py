# Writing the name to "name.txt"
name = input("Enter your name: ")
file_name = "name.txt"

try:
    with open(file_name, 'w') as file:
        file.write(name)
        print("Name successfully written to the file.")
except IOError:
    print("An error occurred while writing to the file.")

# Reading the name from "name.txt" and printing it
try:
    with open(file_name, 'r') as file:
        stored_name = file.read()
        print("Your name is", stored_name)
except FileNotFoundError:
    print("The file could not be found.")
except IOError:
    print("An error occurred while reading the file.")
# Adding the first two numbers from numbers.txt

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()[:2]]

result = sum(numbers)
print("The sum of the first two numbers is:", result)
# Calculating the sum of all numbers in numbers.txt

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

result = sum(numbers)
print("The sum of all numbers is:", result)

