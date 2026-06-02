"""Filter users from a JSON file by age and email."""

import json

USERS_FILE = "users.json"
MINIMUM_AGE = 30
EMAIL_DOMAIN = "example.com"


def load_users(file_path):
    """Load users from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


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
    """Run the user filtering program."""
    users = load_users(USERS_FILE)

    filtered_by_age = filter_users_by_age(users, MINIMUM_AGE)
    print("Users filtered by age:")
    print_users(filtered_by_age)

    filtered_by_email = filter_users_by_email(users, EMAIL_DOMAIN)
    print("\nUsers filtered by email:")
    print_users(filtered_by_email)


if __name__ == "__main__":
    main()
