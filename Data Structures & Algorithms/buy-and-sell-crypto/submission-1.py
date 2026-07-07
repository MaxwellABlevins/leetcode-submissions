class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        low = prices[0]        

        for i, v in enumerate(prices):
            if (v - low) > currentMax:
                currentMax = v - low
            elif v < low:
                low = v
        return currentMax