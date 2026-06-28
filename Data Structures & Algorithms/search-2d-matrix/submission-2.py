class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix) - 1
        mid1 = 0
        mid2 = 0

        while left <= right:
            mid1 = (left + right) // 2
            if target >= matrix[mid1][0] and target <= matrix[mid1][-1]:
                left, right = 0, len(matrix[mid1]) - 1
                
                while left <= right:
                    mid2 = (left + right) // 2
                    if target == matrix[mid1][mid2]:
                        return True
                    if target < matrix[mid1][mid2]:
                        right = mid2 - 1
                        continue
                    if target > matrix[mid1][mid2]:
                        left = mid2 + 1
                        continue
                return False
            
            if target < matrix[mid1][0]:
                right = mid1 - 1
                continue
            if target > matrix[mid1][-1]:
                left = mid1 + 1
                continue
        return False