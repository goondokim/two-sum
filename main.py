from typing import List

def twoSum (nums: list[int], target: int):
    N = len(nums)
    for i in range (0, N):
        for j in range (0, N):
            if (i == j):
                continue
            if ((nums[i]+nums[j]) == target):
                needs = [i, j]
    return needs



    
