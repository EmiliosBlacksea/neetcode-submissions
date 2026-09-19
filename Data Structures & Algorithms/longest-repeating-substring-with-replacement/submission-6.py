class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = [0] * 26
        most_f = 0
        longest_length = 0
        left = 0
        right = 0
        counts[ord(s[right]) - ord('A')] += 1
        while right < len(s):
            
            most_f = max(counts)
            gap = right - left  + 1
            replace = gap - most_f
            if replace <= k:
                right += 1
                if right < len(s):
                    counts[ord(s[right]) - ord('A')] += 1
                longest_length = max(longest_length, gap)
            else:
                if right == len(s) - 1 and longest_length >= gap:
                    return longest_length
                counts[ord(s[left]) - ord('A')] = max(0, counts[ord(s[left]) - ord('A')] - 1)
                left += 1
                if longest_length >= gap:
                    right += 1
                    counts[ord(s[right]) - ord('A')] += 1
        return longest_length


        