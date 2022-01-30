​Plan: Binary search of min value

O(log(N)) Solution:

The sorted array comes with a clockwise rotation of numknown steps

# [ 7, 8 , 9, 1, 2, 3, 4, 5]
        # case 1: mid is at minimum of right sorted array
          return mid value
        # case 2: mid is at maximum of left sorted array
          return mid+1 value
        # case 3: mid is at middle of right sorted array
          set high index to mid
        # case 4: mid is at middle of left sorted array
          set low index to mid
