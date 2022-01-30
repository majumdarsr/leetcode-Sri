​ Plan

O(log(n) * log(n)) solution: 

Worst case is O(n)

1. https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
2. For any number its greatest divisor is its square root
3. Create an array of ones with index 0 to number - 1
4. run loop check for k = 2 to sqrt(number) (O(log(n))
5. If index a multiple of k, replace 1 with 0
6. At the end the array would have ones only at the indexes that are prime.
7. return sum of array[2:]

