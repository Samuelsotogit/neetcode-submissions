class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# The time complexity is O(n) because there are no nested loops and every loop is an O(n) operation. 
# Space complexity is also O(n) because I store N values in each list and hashmap at most.
        if len(s) != len(t):
            return False
        word1_counts = {}
        word2_counts = {}
        for i in range(len(s)):
            word1_counts[s[i]] = word1_counts.get(s[i], 0) + 1
            word2_counts[t[i]] = word2_counts.get(t[i], 0) + 1
        return word1_counts == word2_counts

            