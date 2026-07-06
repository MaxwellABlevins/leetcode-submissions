class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sums = {}
        most = nums[0]

        for v in nums:
            if v in sums:
                sums[v] += 1
            else:
                sums[v] = 1 
            if sums[v] > sums[most]:
                most = v
        return most