import unittest
from onekey import SafeDeposit
from onekey import CLI
import io
import shutil
import os
import sys
import onekey
import getpass

# Filename contains one record: "key" -> "value"
filename = "test/test.psx"
key = "testpass"

def noop(*args, **kws):
	return None

# Mock
getpass.getpass = lambda : "secret"
os.system = noop

class CLIUnitTest(unittest.TestCase):

	def setUp(self):
		shutil.copy("test/test.ts", filename)

	def tearDown(self):
		os.remove(filename)

	def test_command(self):

		safe = SafeDeposit(key, path=filename)
		cli = CLI(safe)
		
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput

		cli.command("list")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertIn("key", output)

		cli.command("del", "key")
		cli.command("list")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertNotIn("key", output)

		cli.command("add", "arctic")
		cli.command("list")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertIn("arctic", output)

		cli.command("view", "arctic")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertIn("secret", output)
		sys.stdout = sys.__stdout__

		cli.command("change", "changedpassword")
		cli.command("clear")
