class Solution {
public:
    // Algorithom from
    // https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
    int countPrimes(int n) {  
        if (n == 0) 
            return 0;
        
        int n_sqrt = round(sqrt(n)); 
        
        int count_prime[n];
        std::fill_n(count_prime, n, 1);

        int k = 2;
        while (k <= n_sqrt){
            if (count_prime[k])
            {
                for (int i = 2*k; i < n; i+=k)
                    count_prime[i] = 0;      
            }
            k++;
        }
        
        int total = 0;
        for (int j = 2; j < n; j++)
            total += count_prime[j];
        
        return total;
        
    }
};