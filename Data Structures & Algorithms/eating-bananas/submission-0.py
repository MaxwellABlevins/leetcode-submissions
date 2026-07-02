class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        mid = (left + right) // 2
        rate = right
        hours = 0

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for b in piles:
                if mid < b:
                    hours += math.ceil(b / mid)
                elif mid >= b:
                    hours += 1
                if hours > h:
                    break
            if hours <= h and mid < rate:
                rate = mid
            elif hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return rate