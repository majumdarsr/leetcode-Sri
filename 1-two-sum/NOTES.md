​Plan:
input : array of nums, target
Solution:
O(n^2):
for idx in index in 0 to -2:
for nidx in index 1 to -1:
check if target matches to nums[idx]+nums[nidx]
return idx, nidx
