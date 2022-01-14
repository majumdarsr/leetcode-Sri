class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # Base cases
        if not nums:
            return 1
        if len(set(nums)) == 1:
            return 1 if list(set(nums))[0] != 1 else 2
        pos_total = 0
        count = 0 # keep count of number of positives
        minPos = -1 #  keep tract of minimum positive present in the list
        for num in set(nums):
            if num > 0:
                pos_total += num
                count += 1
                if minPos == -1:
                    minPos = num
                elif num < minPos:
                    minPos = num

        if minPos != 1: # in case of all positives not a series
            return 1
        elif pos_total == count*(count+1)//2: # an int series, minPos = 1
            return count+1
        else: # minPos == 1 and not a series
            #val = [-1] * (count + 2) # there should be count+1 positives
            valFound = False
            for num in set(nums):
                if num > 1 and num < count: # count is the minimum length of nums
                    nums[num] = num
                    valFound = True
            #print(nums)
            if not valFound:
                return minPos+1
            else:
                for i in range(count): 
                    if i > 1 and nums[i] != i:
                        return i
                return count # in case nothing returned from 2 to count-1
