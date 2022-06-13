#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


"""
WARNING: This script encrypts every file at the Current Working Directory
Use it at your own risk!
"""


def key_setup():
    """
    Checks if key already exists
    """
    if ("my_key.key" in os.listdir()):
        return True
    return False


def create_key():
    key = Fernet.generate_key()
    with open("my_key.key", "wb") as thekey:
        thekey.write(key)


def encrypt(file_to_encrypt, encrypted_content):
    """
    Encrypt every file using contents_encrypted
    """
    with open(file_to_encrypt, "wb") as file:
        file.write(encrypted_content)


def create_encrypted_file(file):
    """
    Reads every file's contents and store their encrypted version
    inside contents_encrypted
    """

    # rb == read binary
    with open(file, "rb") as thefile:
        content = thefile.read()
    encrypted_content = Fernet(key).encrypt(content)
    encrypt(file, encrypted_content)


files = []

# os.listdir() lists every file in cwd
for file in os.listdir():
    if file == "file_encrypter.py" or file == "my_key.key":
        continue

    # if append file() where used here, every dir
    # inside cwd would be encrypted aswell.
    if os.path.isfile(file):
        files.append(file)

print(files)

if key_setup():
    with open("my_key.key", "rb") as key:
        secret_key = key.read()
else:
    # wb == write binary
    create_key()

for file in files:
    create_encrypted_file(file)
