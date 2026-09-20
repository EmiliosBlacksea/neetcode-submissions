class Solution:
    def isPalindrome(self, s: str) -> bool:
        tostring = []
        s.lower()
        print(ord("A"), ord("a"))
        for letter in s:
            
            AZ = ord("A") <= ord(letter) and ord(letter) <= ord("Z")
            az = ord("a") <= ord(letter) and ord(letter) <= ord("z")
            zeronine = ord("0") <= ord(letter) and ord(letter) <= ord("9")

            if AZ or zeronine or az:
                tostring.append(letter)
        left = 0
        right = len(tostring) - 1
        print(tostring)
        while left < right:
            if tostring[left].lower() != tostring[right].lower():
                return False
            left += 1
            right -= 1
        return True