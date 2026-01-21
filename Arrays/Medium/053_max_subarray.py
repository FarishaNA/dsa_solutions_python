# LeetCode 53 – Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Uses Kadane’s Algorithm to find the maximum subarray sum in linear time.(DP)
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
