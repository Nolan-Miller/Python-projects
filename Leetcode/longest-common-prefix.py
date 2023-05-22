'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

This solution beat 36.48% of run times (47 ms) and 42.76% of memory usages (16.3 MB)
'''

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        if not all(s for s in strs):
            return ''
        '''
        pre = min(strs, key=len)
        if pre == 0:
            return ''
        for s in strs:
            while not s.startswith(pre):
                pre = pre[:-1]

        return pre
        
solution = Solution()
strs = []
print("Enter words to the list ('q' to stop)")
word = ''
while True:
    word = input()
    if word == 'q':
        break
    strs.append(word)
prefix = solution.longestCommonPrefix(strs)
print()
if prefix:
    print(f'Longest common prefix: "{solution.longestCommonPrefix(strs)}"')
else:
    print("There is no common prefix between the given words")
