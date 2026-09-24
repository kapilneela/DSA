class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[i]
            s=0

            # taking sum of digits of each element in nums
            while(n!=0):
                s+=(n%10)
                n//=10
            
            # check whether the sum is equal to index
            if s==i:
                #since to return smallest index return it immediately
                return i
        # if no such index exist return -1
        return -1
