num = int(input())
result = []

if i in range(1,num//2):
  if num % i == 0 :
    result.append(i)
result.append(num)
return result
