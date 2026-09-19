class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_char = {}
        start = 0
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] not in sub_char:
                sub_char[s[i]] = i
                length += 1
            else:
                if sub_char[s[i]] < start:
                    length += 1
                    sub_char[s[i]] = i
                else:
                    start = sub_char[s[i]] + 1
                    sub_char[s[i]] = i
                    length = i - start + 1
            max_length = max(max_length, length)              
                
        return max_length
# a b c d w k w e f g h  i  j
# 0 1 2 3 4 5 6 7 8 9 10 11 12

# t m m z u x t
# 0 1 2 3 4 5 6 l = 1 l = 2 