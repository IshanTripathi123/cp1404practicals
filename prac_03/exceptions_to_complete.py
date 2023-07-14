"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True to exit the loop when a valid integer is entered
    except ValueError:  # Catch ValueError exception when a non-number is entered
        print("Please enter a valid integer.")
print("Valid result is:", result)
