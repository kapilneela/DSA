arr = [1,2,3,4,5,3,2,2,1,1,7,7,7,5,6,4]

hash_table = [0] * 10

for num in arr:
  hash_table[num] += 1

print(hash_table)
