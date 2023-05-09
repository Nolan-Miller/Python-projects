class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for curr in range(len(nums)):
            if target - nums[curr] in visited:
                return [visited[target - nums[curr]], curr]
            else:
                visited[nums[curr]] = curr
