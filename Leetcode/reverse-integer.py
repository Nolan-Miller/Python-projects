'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

This solution beat 48.35% of run times (40 ms) and 25.87% of memory usages (16.3 MB)
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = 1
        num = 0
        if x < 0:
            sign = -1
        str_num = str(abs(x))
        str_num = str_num[::-1]
        str_num = re.sub(r'^0?', '', str_num)
        num = int(str_num)
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num * sign
