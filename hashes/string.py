import hashlib

from utils.generate_string import generate_string

def hash_string(string, loops):
  string = ' '.join(format(ord(x), 'b') for x in string).encode('utf-8')

  for _ in range(1, loops):
    string = hashlib.md5(string).hexdigest().encode('utf-8')

  return string
