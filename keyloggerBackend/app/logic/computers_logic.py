import os
from keyloggerBackend.app.logic.decrypt_logic import Decryptor

base_directory = r"C:\devlopment\python\keyloggerProject\keyloggerBackend\data"


def get_names_computer():

    # file_names = [f for f in os.listdir(base_directory) if os.path.isfile(os.path.join(base_directory, f))]
    folder_names = [f for f in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, f))]
    print(folder_names)
    return folder_names

def get_data_by_computer(computer_name):
    data=help_get_data_by_computer(computer_name)
    decrypt = Decryptor()
    decrypted_data = decrypt.decrypt_data(data)
    print(decrypted_data)
    return decrypted_data

def help_get_data_by_computer(computer_name):
    file_path = os.path.join(base_directory, computer_name, "data.json")
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return file.read()