"""Filter users from a JSON file by name, age, and email."""

import json

USERS_FILE = "users.json"


def load_users(file_path):
    """Load users from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(users, name):
    """Return users with the given name."""
    return [
        user
        for user in users
        if user.get("name", "").lower() == name.lower()
    ]


def filter_users_by_age(users, minimum_age):
    """Return users who are at least the given minimum age."""
    return [
        user
        for user in users
        if user.get("age", 0) >= minimum_age
    ]


def filter_users_by_email(users, email_domain):
    """Return users whose email ends with the given domain."""
    return [
        user
        for user in users
        if user.get("email", "").endswith(email_domain)
    ]


def print_users(users):
    """Print users line by line."""
    for user in users:
        print(user)


def main():
    """Ask the user for a filter type and print matching users."""
    users = load_users(USERS_FILE)

    filter_type = input("Filter by name, age, or email: ").lower()

    if filter_type == "name":
        name = input("Enter name: ")
        filtered_users = filter_users_by_name(users, name)

    elif filter_type == "age":
        minimum_age = int(input("Enter minimum age: "))
        filtered_users = filter_users_by_age(users, minimum_age)

    elif filter_type == "email":
        email_domain = input("Enter email domain: ")
        filtered_users = filter_users_by_email(users, email_domain)

    else:
        print("Invalid filter type.")
        return

    print_users(filtered_users)


if __name__ == "__main__":
    main()
