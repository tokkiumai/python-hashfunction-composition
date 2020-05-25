def caesar_cipher(string, s):
  result = ''

  for i in range(len(string)):
    char = string[i]

    if (char.isupper()):
      result += chr((ord(char) + s - 65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)

  return result
