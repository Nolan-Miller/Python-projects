'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

This solution beat 51.98% of run times (78 ms) and 14.8% of memory usages (17.7 MB)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for curr in range(len(nums)):
            if target - nums[curr] in visited:
                return [visited[target - nums[curr]], curr]
            else:
                visited[nums[curr]] = curr
