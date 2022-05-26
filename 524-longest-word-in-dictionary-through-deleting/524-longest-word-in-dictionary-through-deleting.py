class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        import re
        longest = ""
        
        for word in dictionary:
            if word == s:
                return word
            elif len(word) >= len(s):
                continue
            else:
                lenword = len(word) - 1
                idx = len(s) - 1
                
                while idx >= 0 and lenword >= 0:
                    #print(lenword)
                    if word[lenword] == s[idx]:
                        lenword -= 1
                        idx -= 1
                    else:
                        idx -= 1
                    
                    if lenword == -1 and len(word) > len(longest):
                        longest = word
                        break
                    elif lenword == -1 and len(word) == len(longest):
                        if word < longest:
                            longest = word
                        break
                    
        return longest              
                
        