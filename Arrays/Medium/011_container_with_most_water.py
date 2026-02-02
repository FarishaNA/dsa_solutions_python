# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Approach: Two-pointer (Greedy)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation: Start with two pointers at both ends and move the pointer with the smaller height to maximize area.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        low, high = 0, len(height) - 1

        while low < high:
            # Area = min height * width
            curr_area = min(height[low], height[high]) * (high - low)
            max_area = max(max_area, curr_area)

            # Move the pointer with smaller height
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return max_area
