from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This solution has O(n*k) complexity
        groups = defaultdict(list)
        for word in strs: # O(n) 
            counts = [0] * 26
            for letter in word: # O(k)
                counts[ord(letter) - ord('a')] += 1 # O(1)
            groups[tuple(counts)].append(word) # O(1)
        return list(groups.values()) # O(n) worst case
            
        # groups = defaultdict(list)
        # for word in strs: # O(n)
        #     groups["".join(sorted(word))].append(word) # O(klog(k))
        # return list(groups.values())

        # groups = {}
        # for i in range(len(strs)):
        #     sorted_key = sorted(strs[i])
        #     key = "".join(sorted_key)
        #     if key not in groups:
        #         groups[key] = []
        #     groups[key].append(strs[i])
        # result = []
        # for group in groups.values():
        #     result.append(group)
        # return result