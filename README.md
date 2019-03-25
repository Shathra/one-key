# one-key

[![CircleCI](https://circleci.com/gh/Shathra/one-key/tree/master.svg?style=svg)](https://circleci.com/gh/Shathra/one-key/tree/master) [![codecov](https://codecov.io/gh/Shathra/one-key/branch/master/graph/badge.svg)](https://codecov.io/gh/Shathra/one-key)

Command Line Key-Value Storage Application. Stores key-value pairs into a file using AES encryption. Created to practice test driven development.

## Installation

`conda install -c conda-forge --file requirements.txt`

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
