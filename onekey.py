from Crypto.Cipher import AES
from Crypto import Random
import json
import os
import getpass

_DEFAULT_PATH = "lemonade.psx"


class OneKey:

    def __init__(self, master_key, path=_DEFAULT_PATH):
        self.path = path
        self.key_dict = None
        self.master_key = master_key

    def _export_file(self):
        def pad(s):
            s = s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
            return s

        iv = Random.new().read(AES.block_size)
        aes = AES.new(self.master_key, AES.MODE_CBC, iv)
        plain_text = json.dumps(self.key_dict)
        plain_text = pad(plain_text)
        cipher_text = aes.encrypt(plain_text)
        content = iv + cipher_text
        file = open(self.path, "wb")
        file.write(content)
        file.close()

    def import_file(self):
        """
        Import an encrypted file with a given key, deserializes it into a dict.
        """
        def unpad(s):
            s = s[:-ord(s[len(s) - 1:])]
            return s

        file = open(self.path, "rb")
        content = file.read()
        file.close()

        iv = content[:AES.block_size]
        cipher_text = content[AES.block_size:]

        aes = AES.new(self.master_key, AES.MODE_CBC, iv)
        plain_text = aes.decrypt(cipher_text)
        plain_text = unpad(plain_text)
        plain_text = plain_text.decode("utf-8")
        self.key_dict = json.loads(plain_text)

    def command_list(self, arg):
        """
        Returns a list of stored key values.
        :param arg: If none all keys are retrieved, otherwise only keys containing arg will be returned.
        :return: list of keys
        """
        if arg is None:
            retval = [x for x in self.key_dict.keys()]

        else:
            retval = [x for x in self.key_dict.keys() if arg in x]

        return retval

    def command_add(self, key, value):
        """
        Add a value with a given key, and store it
        :param key: key to add
        :param value: Corresponding value
        """
        self.key_dict[key] = value

        self._export_file()

    def command_del(self, key):
        """
        Deletes a key and store changes.
        :param key: key to delete
        """
        self.key_dict.pop(key, None)

        self._export_file()

    def command_view(self, key):
        """
        Returns value with given key
        :param key: key
        :return: value
        """
        retval = None

        if key in self.key_dict.keys():
            retval = self.key_dict[key]

        return retval


def main():

    key = getpass.getpass("Master Key:")
    ok = OneKey(key)

    is_file_exist = os.path.isfile(_DEFAULT_PATH)
    if not is_file_exist:
        ok.key_dict = dict()

    else:
        ok.import_file()

    command = None
    while command != "quit":

        input_arr = input().split()
        command = input_arr[0]
        arg = None
        if len(input_arr) > 1:
            arg = input_arr[1].lower()

        if command == "list":
            key_list = ok.command_list(arg)
            print()
            for key in key_list:
                print(key)

        elif command == "add":
            if len(input_arr) > 1:
                value = getpass.getpass()
                ok.command_add(arg, value)

        elif command == "view":
            if len(input_arr) > 1:
                value = ok.command_view(arg)
                print()
                print(value)

        elif command == "clear":
            os.system('cls||clear')

        elif command == "del":
            ok.command_del(arg)

    os.system('cls||clear')


if __name__ == "__main__":
    main()
