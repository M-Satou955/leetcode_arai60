class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevMap:
                return [i, prevMap[complement]]
            prevMap[n] = i