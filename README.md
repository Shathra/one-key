# one-key

![Travis Build](https://travis-ci.org/Shathra/one-key.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/Shathra/one-key/badge.svg?branch=master)](https://coveralls.io/github/Shathra/one-key?branch=master) [![CircleCI](https://circleci.com/gh/Shathra/one-key/tree/master.svg?style=svg)](https://circleci.com/gh/Shathra/one-key/tree/master)

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
