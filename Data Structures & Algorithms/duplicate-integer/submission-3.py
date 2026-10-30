class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =  set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
# Still brute force because I am making n/x checks for every element which reduces to O(n^2).
        # i = 0
        # for i in range(len(nums)):
        #     j = len(nums) - 1
        #     while i != j:
        #         if nums[i] == nums[j]:
        #             return True
        #         j-=1;
        # return False
# Iterate over the entire array for every element in the array to check for duplicates, avoding unnecessary checks when indices match.
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] == nums[j]:
        #             return True
        # return False