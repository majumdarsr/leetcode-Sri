class Solution:
    def mySqrt(self, x: int) -> int:
        from math import floor
        low = 0
        high = x
        mid = 1 #lowest possible square root of a positive integer 1
   
        # Calculate the smaller value as mid
        # as we are expected to return the floor value
        while mid >= low: 
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = floor(low + high) // 2
        
        # when mid is smaller than low, high is equal to mid, hence the smaller
        return high
      
        