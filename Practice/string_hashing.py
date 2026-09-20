text = "adfgdadsfsesfdsf"
hash_table = [0] * 26

for char in text:
  ascii_val = ord(char)
  idx = ascii_val - 97
  hash_table[idx] += 1

print(hash_table)
