'''
Created by Conrad Bucholtz

Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?


-----MY SOLUTION-----

[SOLUTION]
'''

def is_prime(n):
    if (n>1):
        for d in range(2, int(n**(0.5))+1):
            if (n%d==0):
                return False
        return True
    return False

def nthPrime(n):
    p = 0
    i = 2
    while (True):
        if (is_prime(i)):
            p += 1
            if (p==n):
                return i
        i += 1;
        
print(nthPrime(10001))