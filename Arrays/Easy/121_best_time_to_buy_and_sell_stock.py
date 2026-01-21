# Problem 121: Best Time to Buy and Sell Stock
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Track the minimum price so far and update max profit for each day (GREEDY)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            # Update min_price if current price is lower
            min_price = min(min_price, price)
            # Update profit if selling today is better
            profit = max(profit, price - min_price)
        return profit
