class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        left, right = 0, 1     

        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            else:
                currentMax = max(currentMax, profit)
            right += 1
        return currentMax