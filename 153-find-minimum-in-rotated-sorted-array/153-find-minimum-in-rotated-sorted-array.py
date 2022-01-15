class Solution:
    def findMin(self, nums: List[int]) -> int:
        input_list = nums[:]
        low = 0
        high = len(input_list) - 1
        
        if len(nums) <= 2:
            return min(nums[low], nums[high])
        
        mid = low + (high - low) // 2
        minimum = 0
        while (mid > low):
        # [ 7, 8 , 9, 1, 2, 3, 4, 5]
        # case 1: mid is at minimum of right sorted array
        # case 2: mid is at maximum of left sorted array
        # case 3: mid is at middle of right sorted array
        # case 4: mid is at middle of left sorted array
            if input_list[mid-1] < input_list[mid] < input_list[mid+1] : # case 3, 4
                if input_list[mid] > input_list[high]: # case 4
                    low = mid
                else: # case 3
                    high = mid
            elif input_list[mid-1] > input_list[mid]: # case 1
                if input_list[mid] < input_list[mid+1]: 
                    minimum = mid
                    break
        
            elif input_list[mid] > input_list[mid+1]: # case 2
                if input_list[mid-1] < input_list[mid]:
                    minimum = mid + 1
                    break
            mid = low + (high - low) // 2
        
        return nums[minimum]
        