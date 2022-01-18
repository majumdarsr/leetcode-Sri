class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        } 
        if not s:
            return True
        if len(s) % 2:
            return False
        if s[0] not in char_dict:
            return False
        if s[-1] not in char_dict.values():
            return False
        
        open_char = []

        for char in s:
            if char in char_dict:
                open_char.append(char)
            elif char in char_dict.values():
                if open_char and char == char_dict.get(open_char[-1]):
                    open_char.pop()                    
                else:
                    return False
                
        return not open_char
                        
                