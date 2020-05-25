import hashlib

from utils import format_and_encode, caesar_cipher

def hash_caesar_cipher(string, loops):
  string_length = len(string)

  for _ in range(loops):
    ciphered = caesar_cipher(string, 4)
    string = format_and_encode(ciphered)

    string = hashlib.md5(string).hexdigest()

  return string[:string_length]

print(hash_caesar_cipher('kekshpek', 5))
