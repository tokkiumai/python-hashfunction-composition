import string
import random

def generate_string(string_length, chars = string.ascii_lowercase):
  string = ''

  for _ in range(1, string_length):
    string += random.choice(chars)

  return string
