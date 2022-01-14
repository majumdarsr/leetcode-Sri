class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        
        res = 0
        start, temp = 0, 1
        while start < len(s) and temp <= len(s):
            substr = s[start:temp]
            #print(res, s[start:temp], start, temp)
            if len(substr) == len(set(substr)):
                res = len(substr) if len(substr) > res else res
                temp += 1
            else: 
                start += 1
                
        return res
                
           