# LeetCode 33 - Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
#
# Approach: Modified Binary Search
# Idea: At any point, one half of the array is sorted.
#       Check whether the target lies in the sorted half and discard the other.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                # Target lies within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:
                # Target lies within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
