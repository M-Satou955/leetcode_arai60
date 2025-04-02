class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevMap:
                return [prevMap[complement], i]
            prevMap[n] = i
        raise ValueError('No valid pair of numbers in the input list')