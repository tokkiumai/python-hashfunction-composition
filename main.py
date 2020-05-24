import time
import argparse

fullTime = time.time()

parser = argparse.ArgumentParser(description = 'Arguments...')

parser.add_argument('-s', '--stringL', help = 'String length to hash', required = False)
parser.add_argument('-t', '--hashL', help = 'Hash length to test', required = False)
parser.add_argument('-r', '--maxRAM', help = 'Maximum RAM to use', required = False)
parser.add_argument('-c', '--maxCollisionsNumber', help = 'Collisions number to find', required = False)
args = parser.parse_args()

string_length = int(args.stringL or 12)
hash_length = int(args.hashL or 12)
max_RAM = int(args.maxRAM or 4096)
max_collisions_number = int(args.maxCollisionsNumber or 10)
