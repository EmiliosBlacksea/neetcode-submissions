class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord("a")] += 1
            result[tuple(key)].append(word)
        return (list(result.values()))