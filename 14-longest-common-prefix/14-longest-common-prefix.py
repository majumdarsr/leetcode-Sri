class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # assign prefix to item[0] if item[0] exits else return prefix
        prefix = ""
        
        if strs[0]:
            if strs[0][0]:
                prefix = strs[0][0]            
        else:
            return prefix
        
        prefixEnd = False
        count = 0
        
        while not prefixEnd:
            for item in strs[1:]:
                try: # taking care of out of range issue
                    if prefix[count] != item[count]:
                        prefixEnd = True
                        break
                except:
                        prefixEnd = True
                        break
                    
            if not prefixEnd: 
                count = count + 1
                
                try: # taking care of out of range issue
                    prefix = prefix + strs[0][count]
                except:
                    return prefix
                
            else:
                prefix = prefix[:-1]
            
        return prefix
        
            