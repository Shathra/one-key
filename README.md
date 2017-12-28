# one-key

![Travis Build](https://travis-ci.org/Shathra/one-key.svg?branch=master)

Command Line Key-Value Storage Application. Stores key-value pairs into a file using AES encryption. Created to practice test driven development.

## Usage

`python onekey.py`

### Add

`add <key>`

Asks for value then add it with given key

### List

`list [<argument>]`

Lists keys containing `<argument>` if exist.

### View

`view <key>`

Views the value of given key

### Del

`del <key>`

Deletes entry with given key

### Clear

`clear`

Clears terminal output

### Quit

`quit`

Quits application
