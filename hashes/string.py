import hashlib

from utils import format_and_encode

def hash_string(string, loops):
  string_length = len(string)

  for _ in range(loops):
    string = format_and_encode(string)
    string = hashlib.md5(string).hexdigest()

  return string[:string_length]
