# Problem 1: Two Sum
# LeetCode: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a hashmap to find complement indices in one pass

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}  # number -> index map
        for i, num in enumerate(nums):
            if target - num in m:
                return [i, m[target - num]]
            m[num] = i
