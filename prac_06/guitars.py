class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        current_year = 2023  # Replace this with the actual current year
        age = current_year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50


def test_guitar_methods(guitar):
    age = guitar.get_age()
    expected_vintage = age >= 50

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, age, guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}\n".format(guitar.name, expected_vintage, guitar.is_vintage()))


# Create guitars
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.4)
guitar2 = Guitar("Another Guitar", 2013, 750)

# Test guitar methods
test_guitar_methods(guitar1)
test_guitar_methods(guitar2)
