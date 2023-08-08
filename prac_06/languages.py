"""
CP1404 - Language program
Estimated time: 40minutes
Actual time: 3 hours
"""
from cp1404practicals.prac_06.programming_language import ProgrammingLanguage


def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(python)

    # Print information about each programming language
    print("The dynamically typed languages are:")
    programming_languages = [java, python, visual_basic, ruby]
    for language in programming_languages:
        if language.is_dynamic() is True:
            print(language.name)


main()
