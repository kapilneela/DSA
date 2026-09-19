class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x) # convert -int to +int
        res = 0
        while x >0 :
            res = res* 10 + ( x % 10)
            x //= 10
        if res < -2**31 or res > 2**31 - 1:
            return 0 # check for large int. required to pass 1036 testcase
        res *= sign
        return res
