​Plan: missing smallest positive

O(n) Solution containing many for loops

1. Count positives, save minimum, calculate total of all positives
2. if minimum not 1, return 1 as 1 is the smallest positive number possible
3. if minimum 1 and total is count(count+1)/2, it's a series. return count+1
4. if minimum 1 and not an integer series, write positive numbers on the list index matching the numbers
5. for example [-1, 0, 2, 3, 1, 2] -> [0, 1, 2, 3, 1, 2]
6. return the first index that does not match the value at that index. 
7. For above example the answer is 4
