"""Filter users from a JSON file by age and print the result."""

import json

USERS_FILE = "users.json"
MINIMUM_AGE = 30


def load_users(file_path):
    """Load users from a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        A list of user dictionaries.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_age(users, minimum_age):
    """Return users who are at least the given minimum age.

    Args:
        users: A list of user dictionaries.
        minimum_age: The minimum age a user must have.

    Returns:
        A list of filtered user dictionaries.
    """
    return [
        user
        for user in users
        if user.get("age", 0) >= minimum_age
    ]


def print_users(users):
    """Print users line by line.

    Args:
        users: A list of user dictionaries.
    """
    for user in users:
        print(user)


def main():
    """Run the user filtering program."""
    users = load_users(USERS_FILE)
    filtered_users = filter_users_by_age(users, MINIMUM_AGE)
    print_users(filtered_users)


if __name__ == "__main__":
    main()
