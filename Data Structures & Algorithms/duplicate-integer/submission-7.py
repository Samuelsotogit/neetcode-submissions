class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
# Resolve 1 using a dictionary -> implemented via hash table hence time complexity is O(n) for this solution:
        # seen = {}
        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        # for count in seen.values():
        #     if count > 1:
        #         return True
        # return False
# Resolve 2 using a set -> also implemented using a hashtable, avoids storing unnecessary values.
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False