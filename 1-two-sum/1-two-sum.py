class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for every item in list calculate sum of two numbers
                       
        for idx in range(len(nums)):

            for nidx in range(idx+1, len(nums), 1):
               
                if (nums[idx] + nums[nidx] == target):
                    return [idx, nidx]
        """
        from collections import Counter
        index1 = -1
        index2 = -1 
        numD = Counter(nums)
        for key in numD:
            if numD[key] > 1:
                if (2 * key == target):
                    index1 = nums.index(key)
                    print(index1)
                    index2 = index1 + 1 + nums[index1+1:].index(key)
                    print(index2)
                    return [index1, index2]
            else:
                for key2 in numD:
                    if key != key2:
                        if key + key2 == target:
                            index1 = nums.index(key)
                            index2 = nums.index(key2)
                            return [index1, index2]
        """                       
        
        