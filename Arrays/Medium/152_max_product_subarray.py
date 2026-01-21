# Problem 152 - Maximum Product Subarray (Medium)
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Approach: Dynamic Programming (track max/min product ending at each index)
# Time Complexity: O(n), Space Complexity: O(1)

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = max_global = nums[0]

        for num in nums[1:]:
            # Swap if current number is negative to handle sign change
            if num < 0:
                min_prod, max_prod = max_prod, min_prod

            # Update local max/min product ending at current index
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            # Update global maximum product
            max_global = max(max_global, max_prod)

        return max_global
