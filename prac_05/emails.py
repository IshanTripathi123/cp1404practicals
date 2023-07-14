def main():
    """Collect email addresses and associated names, and print the results."""
    prompt_email = "Email: "
    prompt_confirm_name = "Is your name {name}? (Y/n) "
    prompt_name = "Name: "

    email_to_name = {}
    email = input(prompt_email)

    while email != "":
        name = find_name(email)
        confirm_name = input(prompt_confirm_name.format(name=name)).lower()

        if confirm_name == "n":
            name = input(prompt_name)

        email_to_name[email] = name
        email = input(prompt_email)

    print()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def find_name(email):
    """Extract the name from the email address provided."""
    parts = email.split("@")
    username = parts[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name


main()
