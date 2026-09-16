class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_length = 0
        length = 0
        for number in nums:
            if number - 1 not in numbers:
                length = 1
                while number + 1 in numbers:
                    length += 1
                    number  += 1
                max_length = max(max_length, length)
        return max_length
            
