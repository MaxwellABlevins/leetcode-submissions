class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x
        mid = (left + right) / 2

        while left <= right:
            mid = (left + right) // 2
            midSq = (mid * mid) // 1

            if midSq == x:
                return mid
            if midSq > x:
                right = mid - 1
            if midSq < x:
                left = mid + 1

        return right