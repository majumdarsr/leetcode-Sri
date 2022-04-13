class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_1 = 0
        count_2 =0
        
        for num in nums:
            if num == 1:
                count_1 += 1
            elif num == 2:
                count_2 += 1
                
        count_0 = len(nums) - count_1 - count_2
        
        for i in range(len(nums)):
            if i < count_0:
                nums[i] = 0
            elif i < count_0 + count_1:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums