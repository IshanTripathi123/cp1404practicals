# CP1404/CP5632 Practical
# Colour names and their codes in a dictionary

NAME_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "Alice Blue": "#f0f8ff",
    "Aqua": "#00ffff",
    "Ash Grey": "#b2beb5",
    "Baby Blue": "#89cff0",
    "Baby Pink": "#f4c2c2",
    "Banana Yellow": "#ffe135",
    "Barn Red": "#7c0a02",
    "Black": "#000000",
    "Blue Bell": "#a2a2d0"
}

print(NAME_TO_CODE)

# Prompt the user for a colour name and display the corresponding colour code
colour_name = input("Enter colour name: ").title()

while colour_name != "":
    if colour_name in NAME_TO_CODE:
        colour_code = NAME_TO_CODE[colour_name]
        print(f"{colour_name} has colour code {colour_code}")
    else:
        print("Invalid colour name")

    colour_name = input("Enter colour name: ").title()

print("Finished")
