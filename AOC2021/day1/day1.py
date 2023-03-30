inputFile = open('input.txt', 'r').read().splitlines()

nums = list(map(int, inputFile))

def countIncr(nums):
    prev = nums[0]
    numIncr = 0

    for num in nums:
        if num > prev:
            numIncr += 1
        prev = num

    return numIncr

def countWindows(nums):
    numIncr = 0
    for i in range(3, len(nums)):
        n = sum(nums[:3]) + nums[i] - nums[i - 3]
        if n > sum(nums[:3]):
            numIncr += 1
    return numIncr

    

print(f'part 1: {countIncr(nums)}')
print(f'Part 2: {countWindows(nums)}')
