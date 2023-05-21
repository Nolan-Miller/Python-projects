'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

This solution beat 51.98% of run times (78 ms) and 14.8% of memory usages (17.7 MB)
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for curr in range(len(nums)):
            if target - nums[curr] in visited:
                return [visited[target - nums[curr]], curr]
            else:
                visited[nums[curr]] = curr

solution = Solution()
nums = []
target = 0
print("Enter numbers to add to the list ('q' to stop)")
while True:
    num = input("Add a number to the list: ")
    if num.lower() == 'q':
        break
    if not num.isdigit():
        print("Enter only integer values")
        continue
    nums.append(int(num))
print()
while True:
    target = input("Enter a target value: ")
    if not target.isdigit():
        print("Enter an integer value")
        continue
    target = int(target)
    break
try:
    val1, val2 = solution.twoSum(nums, target)
    print(f"\n{nums[val1]} + {nums[val2]} = {target}")
except:
    print("\ntarget value cannot be reached by addition!")
