from collections import deque

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs) # O(n) time

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s): # O(n) time because i only moves forward, j touches each character once, and the slicing total complexity is spread out over s. So O(n) where n is the number of chars.
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            decoded_strs.append(s[i:i + length]) 
            i = i + length
        return decoded_strs
