import json


with open("users.json", "r") as file:
    users = json.load(file)

def filter_by_age(users, min_age):
    return [user for user in users if user["age"] >= min_age]
filtered_users = filter_by_age(users, 30)

for user in filtered_users:
    print(user)
