
users = [
    {"user_id": 1, "name": "Pedro", "email": "macedodasilva22@gmail.com"},
    {"user_id": 2, "name": "Daniel", "email": "danielstam@gmail.com"},
]


def user_info(user_id):
    for user in users:
        if str(user["user_id"]) == user_id:
            return user
    return None

def add_user(user_id, name, email):
    new_user = {
        "user_id": user_id,
        "name": name,
        "email": email
    }
    users.append(new_user)
    return new_user