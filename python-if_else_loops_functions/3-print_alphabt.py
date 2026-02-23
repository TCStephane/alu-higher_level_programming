#!/usr/bin/python3
import string
excluded_letters = {'q', 'e'}
filtered_alphabet = "".join([letter for letter in string.ascii_lowercase if letter not in excluded_letters])
print(filtered_alphabet)