class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm_key_s1 = [0] * 26
        for letter in s1:
            perm_key_s1[ord(letter) - ord('a')] += 1
        len_s1 = len(s1)
        if len_s1 > len(s2):
            return False
        perm_key = [0] * 26
        for i in range(len_s1):
            perm_key[ord(s2[i]) - ord('a')] += 1
        if perm_key_s1 == perm_key:
            return True 
        left = 0
        for right in range(len_s1, len(s2)):
            perm_key[ord(s2[left]) - ord('a')] = max(0, perm_key[ord(s2[left]) - ord('a')] - 1)
            left += 1
            
            perm_key[ord(s2[right]) - ord('a')] += 1
            if perm_key_s1 == perm_key:
                return True
        return False
            
            