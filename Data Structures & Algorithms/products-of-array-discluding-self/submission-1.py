class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) + O(n) = O(n) total time complexity
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix = postfix * nums[i]
        return result

        # Brute force approach O(n^2) time complexity and O(n) space complexity
        # output = [0] * len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         product *= nums[j]
        #     output[i] = product
        # return output