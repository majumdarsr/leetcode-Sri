​Plan: 
input : array of strings

Output: longest prefix

1. Initiate prefix with first string's first char. 
2. Initiate prefixEnd as False. 
3. match prefix char by char to the rest of the strings.
4. keep count of matched characters.
5. keep adding matched characters at the end of previous (shorter) prefix.
6. Whenever mismatch encountered change prefixEnd to True.
7. return prefix[0:count] 

