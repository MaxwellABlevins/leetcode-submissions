class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        ans = [0] * (2 * length)

        for i, v in enumerate(nums):
            ans[i] = v
            ans[i + length] = v
        return ans