# Problem 238: Product of Array Except Self
# LeetCode: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Store prefix products in the output array, then multiply by suffix products in reverse

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
