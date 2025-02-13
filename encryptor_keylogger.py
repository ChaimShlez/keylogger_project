import json
import base64
from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self,kay="cryptor"):
        self.key=kay
        self.text_encrypto=""

    def encryptor(self,s):
        for i in range(len(s)):
            self.text_encrypto += chr(ord(s[i]) ^ ord(self.key[i % len(self.key)]))


    def process_dict(self, data):
        for k ,v in data.items():
           if isinstance(v, dict):
               self.process_dict(v)
           else:
               self.encryptor(v)

    def encrypt(self,dict_data):
        self.text_encrypto=""
        self.process_dict(dict_data)

    def decrypt(self, enc_data):

        self.text_encrypto = ""
        self.process_dict(enc_data)
        return self.text_encrypto
