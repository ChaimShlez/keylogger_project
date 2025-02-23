import json

class Decryptor:
    def __init__(self, kay="cryptor"):
        self.key = kay

    def xor(self, s):

        return "".join(chr(ord(s[i]) ^ ord(self.key[i % len(self.key)])) for i in range(len(s)))

    def decrypt_data(self, enc_data):
        if isinstance(enc_data, str):
            try:
                enc_data = json.loads(enc_data)  # ניסיון להמיר את המחרוזת ל־dict
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format: Expected a dictionary-like structure.")

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

                decrypted_data[time_key] = decrypted_entry

        return decrypted_data