class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            max_water = max((right - left) * min(heights[left], heights[right]), max_water)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] == heights[right]:
                if heights[left + 1] > heights[right - 1]:
                    left += 1
                else:
                    right -= 1
            else:
                right -= 1
        return max_water


# 6 1 100 2 1 50 6
# 6 6
# 6 50
# 1 50