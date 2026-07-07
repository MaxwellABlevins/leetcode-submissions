class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        left, right = 0, 1     

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            elif (prices[right] - prices[left]) > currentMax:
                currentMax = prices[right] - prices[left]
            right += 1
        return currentMax