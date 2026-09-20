class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word

        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        # 2#we3#say1#:3#yes10#!@#$%^&*()
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            letters = int(s[i:j])
            i = j + 1
            decoded.append(s[i:i + letters])
            i = i + letters
        return decoded


