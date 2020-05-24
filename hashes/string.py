import hashlib

def hash_string(string, loops):
  string = string.encode('utf-8')

  for _ in range(1, loops):
    string = hashlib.md5(string).hexdigest().encode('utf-8')

  return string.decode('utf-8')
