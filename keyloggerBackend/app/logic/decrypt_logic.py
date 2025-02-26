import json

class Decryptor:
    def __init__(self, kay="cryptor"):
        self.key = kay

    def xor(self, s):

        return "".join(chr(ord(s[i]) ^ ord(self.key[i % len(self.key)])) for i in range(len(s)))

    import json

    def decrypt_data(self, enc_data):
        if isinstance(enc_data, str):
            try:
                enc_data = json.loads(enc_data)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format: Expected a dictionary-like structure.")

        decrypted_data = {}

        for time_key, encrypted_list in enc_data.items():
            decrypted_data[time_key] = []

            for encrypted_values in encrypted_list:
                for computer_name, platform_data in encrypted_values.items():
                    for platform, input_value in platform_data.items():
                        decrypted_data[time_key].append([

                            self.xor(platform),
                            self.xor(input_value)
                        ])

        return decrypted_data
