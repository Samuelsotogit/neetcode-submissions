from collections import deque

class Solution:

    def encode(self, strs: List[str]) -> str:
        moded_strings = []
        for string in strs:
            string_deque = deque(string)
            string_length = len(string_deque)
            string_deque.extendleft(["#", str(string_length)])
            moded_strings.append("".join(string_deque))
        return "".join(moded_strings)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            decoded_strs.append(s[i:i + length])
            i = i + length
        return decoded_strs
