class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        dTrips = []
        seen = set()

        for i, v in enumerate(nums):
            L = 0
            R = len(nums) - 1

            while L < R:
                pSum = ((nums[L] + nums[R]) * -1)
                if L == i:
                    L += 1
                    continue
                if R == i:
                    R -= 1
                    continue

                if pSum == v:
                    row = [nums[L], nums[R], v]
                    row.sort()
                    tRow = tuple(row)
                    if tRow not in seen:
                        seen.add(tRow)
                        dTrips.append(row)
                    L += 1
                    R -= 1
                elif pSum > v:
                    L += 1
                elif pSum < v:
                     R -= 1


        return dTrips