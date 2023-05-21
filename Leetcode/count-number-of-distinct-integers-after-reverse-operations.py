'''
You are given an array nums consisting of positive integers.

You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array.

This solution beat 97.28% of all run times (685 ms) and 28.84% of all memory usages (43.3 MB)
'''
from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        '''
        nums_set = set()
        for num in nums:
            nums_set.add(int(str(num)[::-1]))
            nums_set.add(num)
        return len(nums_set)
        '''

        return len(set([int(str(num)[::-1]) for num in nums] + nums))

solution = Solution()
nums = []
print("Enter numbers to add to the list ('q' to stop)")
while True:
    num = input("Enter a number: ")
    if num.lower() == 'q':
        break
    if not num.isdigit():
        print("Enter integer values only")
        continue
    nums.append(int(num))
print(f"Number of distinct numbers in list of original numbers and reversed numbers: {solution.countDistinctIntegers(nums)}")
