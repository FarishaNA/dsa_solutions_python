# 15. 3Sum
# LeetCode: https://leetcode.com/problems/3sum/
# Difficulty: Medium
# Approach: Two-pointer after sorting
# Time Complexity: O(n^2)
# Space Complexity: O(1) extra space (excluding output)
# Explanation: For each number, fix it and use two pointers to find pairs that sum to its negative. Skip duplicates to avoid repeated triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array first

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates for the fixed number
                continue

            target = -nums[i]
            low, high = i + 1, len(nums) - 1

            while low < high:
                curr_sum = nums[low] + nums[high]
                if curr_sum == target:
                    res.append([nums[i], nums[low], nums[high]])
                    # Skip duplicates for low and high
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif curr_sum < target:
                    low += 1
                else:
                    high -= 1

        return res
