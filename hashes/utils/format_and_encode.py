def format_and_encode(string):
  return ' '.join(format(ord(x), 'b') for x in string).encode('utf-8')
