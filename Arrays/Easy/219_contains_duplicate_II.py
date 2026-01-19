# Problem 219: Contains Duplicate II
# LeetCode: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a hashmap to store the last index of each number and check distance <= k

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}  # number -> last seen index
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i
        return False
