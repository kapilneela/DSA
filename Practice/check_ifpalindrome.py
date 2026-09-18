n = int(input())
num = n
result = 0
while num>0:
  id = num % 10
  result= (result*10) + id
  num = num//10

return n == result
