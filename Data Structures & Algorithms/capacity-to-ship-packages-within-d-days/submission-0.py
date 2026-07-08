class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)
        mid = (left + right) // 2

        def possibleToShipInTime(capacity: int) -> bool:
            daysWeight = 0
            dayCount = 1

            for v in weights:
                if (daysWeight + v) <= capacity:
                    daysWeight += v
                else: 
                    dayCount += 1
                    daysWeight = v
            return dayCount <= days

        while left <= right:
            mid = (left + right) // 2
            if possibleToShipInTime(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left