import unittest
from onekey import SafeDeposit
from onekey import CLI
import io
import shutil
import os
import sys
import onekey
import getpass

import pyperclip

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

		cli.command("delete", "key")
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

	def test_command_alias(self):
		safe = SafeDeposit(key, path=filename)
		cli = CLI(safe)
		
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput

		cli.command("ls")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertIn("key", output)

		cli.command("del", "key")
		cli.command("ls")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertNotIn("key", output)

		cli.command("add", "arctic")
		cli.command("list")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertIn("arctic", output)

		cli.command("vw", "arctic")
		output = capturedOutput.getvalue()
		capturedOutput.truncate(0)
		self.assertIn("secret", output)
		sys.stdout = sys.__stdout__

		cli.command("ch", "changedpassword")
		cli.command("cls")

	def test_command_copy(self):

		command_lst = ["cp", "copy", "copyforget", "cpf"]

		def cli_command(command):
			safe = SafeDeposit(key, path=filename)
			cli = CLI(safe)

			cli.command(command, "key")

		try:
			pyperclip.paste()
		except pyperclip.PyperclipException:
			# copy-paste not supported, app should not crash
			for command in command_lst:
				cli_command(command)
		else:
			initial_clipboard_value = pyperclip.paste()

			for command in command_lst:
				cli_command(command)
				self.assertEqual("value", pyperclip.paste())

			pyperclip.copy(initial_clipboard_value)