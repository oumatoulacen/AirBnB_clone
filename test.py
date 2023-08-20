#!/usr/bin/python3
'''only tests'''


import shlex


input_string = '"name": "John", "age": 89'

tokens = input_string.split(",")[0].split(":")
print(tokens)


