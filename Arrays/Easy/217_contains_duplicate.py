# Problem 217: Contains Duplicate
# LeetCode: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Compare the length of the list with the length of the set to detect duplicates

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
