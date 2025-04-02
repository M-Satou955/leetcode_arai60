class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[n] = i
        raise ValueError('No valid pairs of numbers in the input list')