class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        left = 0

        for i, v in enumerate(nums):
            if abs(i - left) <= k:
                if v in window:
                    return True
                else: 
                    window.add(v)
            else:
                window.remove(nums[left])
                left += 1
                if v in window:
                    return True
                else:
                    window.add(v)
        return False
