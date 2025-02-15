import json
import base64
from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self,kay="cryptor"):
        self.key=kay



    def xor(self, s):

        return "".join(chr(ord(s[i]) ^ ord(self.key[i % len(self.key)])) for i in range(len(s)))

    def encrypt(self, data):

        data_xor = {}
        for key, value in data.items():
            processed_key = self.xor(key)
            data_xor[processed_key] = {}

            if isinstance(value, dict):

                data_xor[processed_key] = {
                    self.xor(sub_key): self.xor(sub_value) for sub_key, sub_value in value.items()
                }
            else:
                data_xor[processed_key] = self.xor(value)

        return data_xor


    def decrypt(self, enc_data):
        decrypted_data = {}

        for time_key, encrypted_list in enc_data.items():
            decrypted_data[time_key] = {}

            for encrypted_values in encrypted_list:
                decrypted_entry = {}

                for key, value in encrypted_values.items():
                    processed_key = self.xor(key)

                    if isinstance(value, dict):
                        decrypted_entry[processed_key] = {
                            self.xor(sub_key): self.xor(sub_value) for sub_key, sub_value in value.items()
                        }


                decrypted_data[time_key]=decrypted_entry

        return decrypted_data
