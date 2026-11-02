class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            sorted_key = sorted(strs[i])
            key = "".join(sorted_key)
            if key not in groups:
                groups[key] = []
            groups[key].append(strs[i])
        result = []
        for group in groups.values():
            result.append(group)
        return result