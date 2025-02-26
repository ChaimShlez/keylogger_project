import json
import os
from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv

load_dotenv()


TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY")

file_path = r"C:\devlopment\python\keyloggerProject\keyloggerBackend\app\dal\users.json"


def check_login(username, password):
    users = load_users()

    if username in users and users[username]["password"] == password:
        public_id = users[username].get("public_id", username)
        exp_time = datetime.now(timezone.utc) + timedelta(minutes=30)
        token = jwt.encode({
            'public_id': public_id,
            'exp':  exp_time
        }, TOKEN_SECRET_KEY, algorithm="HS256")

        return token

    return False

def load_users():
    # file_path = os.path.join("keyloggerBackend", "app", "dal", "users.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path } does not exist.")
    with open(file_path, "r") as file:
        return json.load(file)
