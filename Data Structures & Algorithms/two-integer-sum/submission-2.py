class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = target
        num_index_dict = {}
        for i in range(len(nums)):
            num_index_dict[nums[i]] = i
        for i, num in enumerate(nums):
            remainder = t - num
            if remainder in num_index_dict and num_index_dict[remainder] != i:
                return [i, num_index_dict.get(remainder)]
            else:
                continue
