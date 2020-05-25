import time
import psutil
import argparse

from utils import generate_string, print_info, cls

from hashes import hash_string

start_time = time.time()

parser = argparse.ArgumentParser(description = 'Arguments...')

parser.add_argument('-s', '--stringL', help = 'String length to hash', required = False)
parser.add_argument('-t', '--hashL', help = 'Hash length to test', required = False)
parser.add_argument('-r', '--maxRAM', help = 'Maximum RAM to use', required = False)
parser.add_argument('-c', '--maxCollisionsNumber', help = 'Collisions number to find', required = False)
parser.add_argument('-trace', '--trace', help = 'Show info messages in console', required = False)
parser.add_argument('-loops','--loops', help = 'Loops to hash', required = False)
args = parser.parse_args()

STRING_LENGTH = int(args.stringL or 12)
HASH_LENGTH = int(args.hashL or 12)
MAX_RAM = int(args.maxRAM or 4096)
MAX_COLLISIONS_NUMBER = int(args.maxCollisionsNumber or 1)
SHOULD_TRACE = args.trace or False 
LOOPS_TO_HASH = int(args.loops or 5)

def show_init_info():
  print (
    'Params: \n\n' + 
    'String length: %s \nHash length: %s \nMax RAM: %s \nMax collisions number: %s'
    %(STRING_LENGTH, HASH_LENGTH, MAX_RAM, MAX_COLLISIONS_NUMBER)
  )


def control_or_store(key, value):
  global hashmap

  if key in hashmap and hashmap.get(key) != value:
    global collisions

    collisions.update({ hashmap.get(key) : value })

    print('Collision detected.')
    print('Hash 1: ' + key + ' with value of ' + value)
    print('Hash 2: ' + key + ' with value of ' + value)

    print('In ' + str(time.time() - start_time) + ' seconds')

    return True
  else:
    hashmap.update({ key: value })
    return False

cls()
show_init_info()

collisions_number = 1
test_number = 0

hashmap = { '' : '' }
collisions = { '' : '' }

hashmap.clear()

while collisions_number <= MAX_COLLISIONS_NUMBER:
  virtual_memory = psutil.virtual_memory()
  virtual_memory = str(virtual_memory)

  virtual_memory = virtual_memory[55:57]
  virtual_memory = int(virtual_memory)

  test_number += 1

  if SHOULD_TRACE and test_number % 100000 == 0:
    print_info(test_number, virtual_memory, collisions_number, len(hashmap), start_time)

  string1 = generate_string(STRING_LENGTH)
  string2 = generate_string(STRING_LENGTH)

  hash1 = hash_string(string1, LOOPS_TO_HASH)
  hash2 = hash_string(string2, LOOPS_TO_HASH)

  if control_or_store(hash1, string1) or control_or_store(hash2, string2):
    collisions_number += 1

  if virtual_memory > MAX_RAM:
    print('Stopping... Too much RAM was used.')
    break

end_time = time.time()
execution_time = end_time - start_time

print('Stopping...')
print('List of collisions found: \n' + str(collisions.items()))
print('Execution time: ' + str(execution_time))
