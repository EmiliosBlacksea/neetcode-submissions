class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        C_S = {}
        C_T = {}
        s_l = len(s)
        t_l = len(t)
        if s_l != t_l: return False
        for i in range(s_l):
            if s[i] not in C_S:
                C_S[s[i]] = 1
            else:
                C_S[s[i]] += 1
            if t[i] not in C_T:
                C_T[t[i]] = 1
            else:
                C_T[t[i]] += 1
        return C_T == C_S
            