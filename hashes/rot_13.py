import hashlib
import codecs

from utils import format_and_encode

def hash_rot_13(string, loops):
  string_length = len(string)
  
  for _ in range(loops):
    translated = codecs.encode(string, 'rot_13')
    string = format_and_encode(translated)

    string = hashlib.md5(string).hexdigest()
  
  return string[:string_length]
