#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


"""
File decrypter using 'my_key.key' created in file_encrypter.py
"""


def key_setup():
    """
    Checks if key already exists
    """
    if ("my_key.key" in os.listdir()):
        return True
    return False


def decrypt(file_to_decrypt, secret_key):
    with open(file_to_decrypt, "rb") as file:
        content = file.read()
    contents_decrypted = Fernet(secret_key).decrypt(content)

    with open(file_to_decrypt, "wb") as file:
        file.write(contents_decrypted)


files = []

# os.listdir() lists every file in cwd
for file in os.listdir():
    if file == "file_encrypter.py" or file == "my_key.key" or file == "file_decrypter.py":
        continue

    if os.path.isfile(file):
        files.append(file)

print(f'Files to be decrypted: {files}')

if key_setup():
    with open("my_key.key", "rb") as key:
        secret_key = key.read()
else:
    print("File 'my_key.key' is missing. Decryption failed.")
    quit()

for file in files:
    decrypt(file, secret_key)
