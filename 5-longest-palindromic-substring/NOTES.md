​Plan: Using hint on leetcode description

1. palindrome can be even or odd lengthed. 
2. starting at one character, or two neighboring characters
3. check if we can grow palindrome by adding characters on both sides
4. odd lengthed racecar, when starts at e, all growing substrings are palindromic: e, cec, aceca, racecar
5. even lengthed AACBBCAA, when starts at BB, all bigger strings are palindromic: BB, CBBC, ACBBCA, AACBBCAA
6. Use a function to check length of longest grown palindrome using above strategy. (Uses a loop and if else conditional)
7. Save start and end indexes for all the maximally grown palindromes, for later use. (this uses a for loop and above function containing a second loop)
8. return longest palindrome. using shurtest start and largest end.
