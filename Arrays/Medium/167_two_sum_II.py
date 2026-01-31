# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
#
# Approach: Two Pointers
# Since the array is sorted, move pointers based on whether the current sum
# is greater or smaller than the target.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                # LeetCode expects 1-based indexing
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
