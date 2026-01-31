# 153. Find Minimum in Rotated Sorted Array
# Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Approach: Binary Search — at each step, compare middle element with high to determine which half contains the minimum
# Time Complexity: O(log n), Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                # Minimum is in the right half
                low = mid + 1
            else:
                # Minimum is in the left half including mid
                high = mid

        return nums[low]
