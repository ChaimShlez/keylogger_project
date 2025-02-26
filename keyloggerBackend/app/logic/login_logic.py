import json
import os
from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv
from numpy.f2py.auxfuncs import throw_error

from errors.erros_types import ErrorsTypes
from exceptions.server_exception import ServerException

load_dotenv()


TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY")

file_path = r"C:\devlopment\python\keyloggerProject\keyloggerBackend\app\dal\users.json"



def check_login(user_name, password):
    users = load_users()
    validate_user_name(user_name,password)
    if user_name in users and users[user_name]["password"] == password:
        public_id = users[user_name].get("public_id", user_name)
        exp_time = datetime.now(timezone.utc) + timedelta(minutes=30)
        token = jwt.encode({
            'public_id': public_id,
            'exp':  exp_time
        }, TOKEN_SECRET_KEY, algorithm="HS256")

        return token
    raise ServerException(ErrorsTypes.LOGIN_FAILURE,"filed login",  f"{user_name}  {password}" )



def load_users():

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path } does not exist.")
    with open(file_path, "r") as file:
        return json.load(file)

def validate_user_name(username,password):
    if not username:
        raise ServerException(ErrorsTypes.USER_NAME_IS_NULL,"user name is empty",+username)

    if not password:
        raise ServerException(ErrorsTypes.PASSWORD_IS_NULL,"password is empty",+password)

