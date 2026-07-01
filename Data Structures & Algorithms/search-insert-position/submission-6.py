class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        mid = (right + left) // 2
        closest_dis = 0
        closest = mid
        
        if (nums[mid] - target) < 0:
            closest_dis = -1 * (nums[mid] - target)
        else:
            closest_dis = nums[mid] - target

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if (target - nums[mid]) < closest_dis:
                    closest = mid
                left = mid + 1
            if nums[mid] > target:
                if (nums[mid] - target) < closest_dis:
                    closest = mid
                right = mid - 1

        if nums[closest] > target:
            if closest == 0:
                return 0
            else:
                return closest
        else:
            return closest + 1
