import json
import os

file_path = r"C:\devlopment\python\keyloggerProject\keyloggerBackend\app\dal\users.json"


# file_path = os.path.join("keyloggerBackend", "app", "dal", "users.json")

# user_file="users.json"



def check_login(username, password):
    user=load_users()
    if username in user and user[username]["password"]==password:
        return True
    return False





def load_users():
    # file_path = os.path.join("keyloggerBackend", "app", "dal", "users.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path } does not exist.")
    with open(file_path, "r") as file:
        return json.load(file)
