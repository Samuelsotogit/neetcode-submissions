class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            remainer = target - num
            if remainer in seen:
                return [seen[remainer], i]
            seen[num] = i

