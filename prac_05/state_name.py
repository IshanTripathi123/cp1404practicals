CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

# Loop to print all states and names neatly lined up
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3s} is {state_name}")

while True:
    state_code = input("Enter short state (or press Enter to exit): ").upper()

    if state_code == "":
        break

    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")

# Loop to print all states and names neatly lined up
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3s} is {state_name}")
