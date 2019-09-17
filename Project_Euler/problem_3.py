'''
Created by Conrad Bucholtz, 9/21/2018

Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?



-----MY SOLUTION-----

First, create a function to return the prime factorization of n in an array
'''

import math

def primeFactorization(n):
    x = n
    primeFactors = []
    while (x > 1): #x will be broken down until it = 1
        for i in range(2, int(math.sqrt(n))+1): #iterate from 2 to sqrt(n)
            if (x%i == 0): #if i divdes evenly, it is a prime factor
                x = int(x/i)
                primeFactors.append(i) #add i to prime factors
                break
            elif (i == int(math.sqrt(n))): #if loop completes, x is prime
                primeFactors.append(x)
                x /= x
    return primeFactors

'''
The largest prime factor will always be the last value in the array so just
print out that value for the given n
'''

a = (primeFactorization(600851475143))
print(a[len(a)-1])
    