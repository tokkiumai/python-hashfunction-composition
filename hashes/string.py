import hashlib

def hash_string(string, loops):
  string_length = len(string)

  for _ in range(1, loops):
    string = ' '.join(format(ord(x), 'b') for x in string).encode('utf-8')
    string = hashlib.md5(string).hexdigest()

  return string[:string_length]
