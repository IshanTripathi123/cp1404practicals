"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ans: when the denominator contains letter instead of number.
2. When will a ZeroDivisionError occur?
ans: when the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
ans: yes we can change the code to avoid the possibility of a ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")