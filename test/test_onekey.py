import unittest
from onekey import OneKey
import shutil
import os

filename = "test.psx"
key = "keymust16bytelon"


class OneKeyUnitTest(unittest.TestCase):

    def setUp(self):
        shutil.copy("test/test.ts", filename)

    def tearDown(self):
        os.remove(filename)

    def test_travis(self):
        self.assertEqual(True, False)

    def test_import_file(self):
        onekey = OneKey(key, path=filename)
        onekey.import_file()

        key_dict = onekey.key_dict

        self.assertEqual("value", key_dict["key"])

    def test_command_list(self):
        onekey = OneKey(key, path=filename)
        onekey.import_file()

        c_list = onekey.command_list(None)
        no = len(c_list)
        self.assertEqual(1, no)

        self.assertIn("key", c_list)

        c_list = onekey.command_list("k")
        no = len(c_list)
        self.assertEqual(1, no)

        self.assertIn("key", c_list)

        c_list = onekey.command_list("a")
        no = len(c_list)
        self.assertEqual(0, no)

    def test_command_add(self):
        onekey = OneKey(key, path=filename)
        onekey.import_file()

        onekey.command_add("gandalf", "You shall not pass")

        onekey = OneKey(key, path=filename)
        onekey.import_file()
        self.assertEqual(onekey.key_dict["gandalf"], "You shall not pass")
        self.assertEqual(onekey.key_dict["key"], "value")

    def test_command_del(self):
        onekey = OneKey(key, path=filename)
        onekey.import_file()

        onekey.command_del("key")

        onekey = OneKey(key, path=filename)
        onekey.import_file()

        count = len(onekey.key_dict.keys())
        self.assertEqual(0, count)

    def test_view(self):
        onekey = OneKey(key, path=filename)
        onekey.import_file()

        value = onekey.command_view("ke")
        self.assertEqual(None, value)

        value = onekey.command_view("key")
        self.assertEqual("value", value)

    def test_add_and_view(self):
        onekey = OneKey(key, path=filename)
        onekey.import_file()

        onekey.command_add("hi", "hello")
        onekey_test = OneKey(key, path=filename)
        onekey_test.import_file()

        value = onekey.command_view("hi")
        self.assertEqual("hello", value)


if __name__ == '__main__':
    unittest.main()
