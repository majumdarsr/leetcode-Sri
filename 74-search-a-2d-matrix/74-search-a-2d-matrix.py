class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        # search target in a specific row
        def findTarget(row, target):
            if row[0] == target or row[-1] == target:
                return 1
            low = 0
            high = len(row) - 1
            mid = low + (high-low) // 2
            while mid > low:
                if target == row[mid]:
                    return 1
                elif target < row[mid]:
                    high = mid
                else:
                    low = mid
                mid = low + (high-low) // 2
      
            if target == row[mid]:
                return 1
            else:
                return 0
            
        # main code: find the row in matrix containing target  
        row_idx = -1
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                row_idx = i
                break
      
        if row_idx == -1: # target out of range
            return 0
        else: # use findTarget to perform a binary search in row
            return findTarget(matrix[row_idx], target)
        