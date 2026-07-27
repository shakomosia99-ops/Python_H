import requests


def get_user(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    for user in users:
        if user["id"] == user_id:
            return {
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"]
            }

    return None


print(get_user(1))
print(get_user(5))
print(get_user(999))
