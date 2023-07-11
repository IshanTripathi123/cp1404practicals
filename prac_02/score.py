import random

MIN_SCORE = -10
MAX_SCORE = 110


def main():
    score: float = 0
    score = round(float(generate_score()), 2)
    print(score)
    print(sort_score(score))


def sort_score(a):
    if a < 0 or a > 100:
        return "Invalid score"
    elif a >= 90:
        return "Excellent"
    elif a >= 50:
        return "Passable"
    else:
        return 'Bad'


def generate_score():
    return float(random.uniform(MIN_SCORE, MAX_SCORE))


main()
