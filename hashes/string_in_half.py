import hashlib

from utils import format_and_encode

def hash_string_in_half(string, loops):
  string_length = len(string)

  for _ in range(1, loops):
    string = format_and_encode(string)
    
    part1  = string[0:string_length//2]
    part2 = string[string_length//2 if string_length%2 == 0 else ((string_length//2)+1):]

    string = hashlib.md5(part1).hexdigest() + hashlib.md5(part2).hexdigest()

  return string[:string_length]
