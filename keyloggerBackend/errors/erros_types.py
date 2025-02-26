
from enum import Enum

class ErrorsTypes(Enum):
    GENERAL_ERROR = (600, "There seems to be a problem, please try again later", True)
    PASSWORD_IS_NULL = (601, "The password is null, please try another one", False)
    INVALID_USER_NAME = (602, "Invalid user name, please try another one", False)
    USER_NAME_IS_NULL = (603, "The user name is null, please try another one", False)
    INVALID_PHONE_NUMBER = (604, "Invalid phone number, please try another one", False)
    USER_ALREADY_EXIST = (605, "The user name already exists, please enter another user name", False)
    USER_NAME_ALREADY_EXIST = (606, "The user name already exists", False)
    INVALID_ADDRESS = (607, "Invalid address, please try another one", False)
    ADDRESS_IS_NULL = (608, "The address is null, please try another one", False)
    LOGIN_FAILURE = (614, "Login failure, user name or password is wrong", False)

    def __init__(self, code, message, loggable):
        self.code = code
        self.message = message
        self.loggable = loggable
