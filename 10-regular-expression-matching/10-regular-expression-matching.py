class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        
        str_list = re.findall(p, s)
        print(str_list)
        
        if not len(str_list):
            return False
        
        '''
        if len(str_list) == 1:
            if s== str_list[0]:
                return True
        '''

        if len(str_list) > 0:
            if s in str_list:
                return True
            
        return False
        
        
            