'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        maxes = []
        for num in nums:
            if num in freq:
                freq[num]+= 1
            else:
                freq[num] = 0
        for i in range(k):
            kmax = max(freq, key = freq.get)
            maxes.append(kmax)
            freq.pop(kmax)
        return maxes

solution = Solution()
nums = []
k = 0
print("Enter integers to add to the list ('q' to stop)")
while True:
    num = input("Enter an integer: ")
    if num.lower() == 'q':
        break
    nums.append(int(num))
while True:
    k = input("Enter a k value: ")
    if not k.isdigit():
        print("Enter an integer value")
        continue
    k = int(k)
    if k > len(set(nums)):
        print("k value cannot be larger than the number of distinct elements")
        continue
    break
most_freq = solution.topKFrequent(nums, k)
print(f"Most common elements: {' '.join(str(num) for num in most_freq)}")
