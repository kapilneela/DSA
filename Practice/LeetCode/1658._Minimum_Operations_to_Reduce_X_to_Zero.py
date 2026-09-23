class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        maxlen = -1
        curr = 0
        l1 = 0

        for r1 in range(len(nums)):
            curr += nums[r1]

            while l1 <= r1 and curr > target:
                curr -= nums[l1]
                l1 += 1

            if curr == target :
                maxlen = max(maxlen, r1- l1 +1)
            
        return len(nums) - maxlen if maxlen != -1 else -1

        
