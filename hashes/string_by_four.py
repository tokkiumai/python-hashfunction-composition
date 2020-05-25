import hashlib

from utils import format_and_encode, split_every_n

def hash_string_by_four(string, loops):
  string_length = len(string)

  for _ in range(1, loops):
    splitted = split_every_n(string, 4)

    new_hash = ''

    for item in splitted:
      item = format_and_encode(item)
      new_hash += hashlib.md5(item).hexdigest()

    string = new_hash

  return string[:string_length]
