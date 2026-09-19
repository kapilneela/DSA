#frequency mapping using dictionary
nums = [5,6,7,5,6,3,5,4,3,4,5,1,1,1,4,5,9,8,7]
freq_map = {}

for i in range(0,len(nums)):
  if nums[i] in freq_map:
    freq_map[nums[i]] += 1
  else:
    freq_map[nums[i]] = 1

print(freq_map)
  
