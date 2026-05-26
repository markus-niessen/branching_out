import json


with open("users.json", "r") as file:
    users = json.load(file)


def filter_by_age(users, min_age):
    return [user for user in users if user["age"] >= min_age]


def filter_by_email(users, email):
    return [user for user in users if user["email"] == email]


filtered_by_age = filter_by_age(users, 30)

print("Users filtered by age:")
for user in filtered_by_age:
    print(user)

filtered_by_email = filter_by_email(users, "anna@example.com")

print("\nUsers filtered by email:")
for user in filtered_by_email:
    print(user)
