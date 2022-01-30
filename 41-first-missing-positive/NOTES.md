​Plan: missing smallest positive

O(n) Solution containing many for loops

1. Count positives, save minimum, calculate total of all positives
2. if minimum not 1, return 1 as 1 is the smallest positive number possible
3. if minimum 1 and total is count(count+1)/2, it's a series. return count+1
4. if minimum 1 and not an integer series, 
