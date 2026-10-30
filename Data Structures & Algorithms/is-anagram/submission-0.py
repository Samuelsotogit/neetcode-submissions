class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word1 = list(s)
        word2 = list(t)
        word1_counts = {}
        word2_counts = {}
        for char in word1:
            word1_counts[char] = word1_counts.get(char, 0) + 1
        for char in word2:
            word2_counts[char] = word2_counts.get(char, 0) + 1
        return word1_counts == word2_counts

            