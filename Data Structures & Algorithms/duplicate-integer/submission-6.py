class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
# Resolve 1:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for count in seen.values():
            if count > 1:
                return True
        return False