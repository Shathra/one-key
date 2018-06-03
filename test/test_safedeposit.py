import unittest
from onekey import SafeDeposit
import shutil
import os

# Filename contains one record: "key" -> "value"
filename = "test.psx"
key = "testpass"


class SafeDepositUnitTest(unittest.TestCase):

    def setUp(self):
        shutil.copy("test/test.ts", filename)

    def tearDown(self):
        os.remove(filename)

    def test_continuous_integration(self):
        self.assertEqual(True, True)

    def test_correct_login(self):
        safe = SafeDeposit(key, path=filename)

    def test_incorrect_login(self):
        try:
            safe = SafeDeposit("falsepasswordpad", path=filename)
            self.fail("False password did not raise Exception")
        except ValueError as err:
            pass

        try:
            safe = SafeDeposit("false_password", path=filename)
            self.fail("False password did not raise Exception")
        except ValueError as err:
            pass

    def test_list(self):
        safe = SafeDeposit(key, path=filename)

        c_list = safe.list(None)
        no = len(c_list)
        self.assertEqual(1, no)

        self.assertIn("key", c_list)

        c_list = safe.list("k")
        no = len(c_list)
        self.assertEqual(1, no)

        self.assertIn("key", c_list)

        c_list = safe.list("a")
        no = len(c_list)
        self.assertEqual(0, no)

    def test_add(self):
        safe = SafeDeposit(key, path=filename)

        safe.add("gandalf", "You shall not pass")

        safe = SafeDeposit(key, path=filename)
        self.assertEqual(safe.key_dict["gandalf"], "You shall not pass")
        self.assertEqual(safe.key_dict["key"], "value")

    def test_remove(self):
        safe = SafeDeposit(key, path=filename)

        safe.remove("key")

        safe = SafeDeposit(key, path=filename)

        count = len(safe.key_dict.keys())
        self.assertEqual(0, count)

    def test_view(self):
        safe = SafeDeposit(key, path=filename)

        value = safe.view("ke")
        self.assertEqual(None, value)

        value = safe.view("key")
        self.assertEqual("value", value)

    def test_add_and_view(self):
        safe = SafeDeposit(key, path=filename)

        safe.add("hi", "hello")
        safe_test = SafeDeposit(key, path=filename)

        value = safe.view("hi")
        self.assertEqual("hello", value)

    def test_change_password(self):
        safe = SafeDeposit(key, path=filename)

        new_password = "white rabbit"
        safe.change_password(new_password)

        safe = SafeDeposit(new_password, path=filename)
        try:
            safe = SafeDeposit(key, path=filename)
            self.fail("False password did not raise Exception")
        except ValueError as err:
            pass


if __name__ == '__main__':
    unittest.main()
