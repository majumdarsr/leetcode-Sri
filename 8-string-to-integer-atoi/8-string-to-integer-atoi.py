class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.strip()
        temp = '1'
        
        if not s:
            return 0
        elif s[0] in ('-', '+'):
            temp = s[0] + temp
            s = s[1:]
            
        lower = -2**31 
        
        try:
            import re
            num = int(re.split('\D', s)[0]) * int(temp)
            if num <= 0:
                return max(lower, num)
            else:
                return min(num, (-1) * lower - 1)
        except ValueError:
            return 0
        