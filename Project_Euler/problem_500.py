'''
Created by Conrad Bucholtz, 9/18/2018

Problem 500:

Find the smallest number with 2^500500 divisors.
Give your answer modulo 500500507.
'''

import math

'''
MY SOLUTION

First, experiment to find the first few smallest 2^n divisors

2^1 divisors = 2
2^2 divisors = 6
2^3 divisors = 24
2^4 divisors = 120
2^5 divisors = 840
2^6 divisors = 7560

Then, look at a factorization of these numbers
(note: not prime factorization)

2    =   2
6    =   2 * 3
24   =   2 * 3 * 4
120  =   2 * 3 * 4 * 5
840  =   2 * 3 * 4 * 5 * 7
7560 =   2 * 3 * 4 * 5 * 7 * 9

We can see, each number multiplies a new, larger factor that cannot be
created by multiplying any of the previous factors together

This makes sense because these new multipliers can create new factors with
each previous combination of multiples, resulting in 2 times more divisors

Only prime and square numbers can have this property
However, not all squares have this property

For example,
36  =  6 * 6
but also 4 * 9, which are previously used factors
therefore, squares with non-prime roots (eg. 6) shouldn't be included

HOWEVER,
16  =  4 * 4
4 is not prime, but 16 SHOULD be included because it cannot be created
using previous factors
therefore, square with roots that have roots that are prime, should be included
(note: this logic is recursive)

Using this observation, we can determine that all new, larger factors must be
    1. Prime
    2. Square with prime/eventually prime roots
    
nextNewFactor(n) finds the smallest number greater than n that satisfies these
parameters
'''

def nextNewFactor(n): #n is the most recent new factor
    i = n+1 #start at the next integer after n
    while (True): #iterate indefinitely
        if isPrime(i):
            return i
        elif isPrimeSquare(i):
            return i
        i += 1

'''
isPrime(n) returns whether n is prime

isPrimeSquare(n) recursively checks n for being a square and having prime roots
'''

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPrimeSquare(n):
    if math.sqrt(n).is_integer(): #check if square
        if isPrime(math.sqrt(n)): #check if the roots are prime
            return True
        elif isPrimeSquare(math.sqrt(n)): #or if the roots of the roots are
            return True
    else:
        return False

'''
smallest2toNDivs(n) the smallest number with 2^n divisors
'''

def smallest2toNDivs(n):
    x=1; #return variable
    y=0; #y keeps track of the latest new factor
    for i in range(n+1): #iterate n+1 times
        y = nextNewFactor(y) #get the next factor
        x *= y #multiply
    return x

'''
Finally, the last function allows for the extremely large number to be handled
The actual number with 2^500500 factors would be much too large to handle

This identity is useful:
(a * c) % b = (a % b) * c

Basically, it allows modulo to be used after every new multiplication
so that the numbers can stay at a manageable size
'''

def smallest2toNDivsMod(n, a): #same function with modulo
    x=1
    y=0
    for i in range(n+1):
        #print(i) #uncomment for calculation progress
        y = nextNewFactor(y)
        x *= y
        x %= a #modulo after every new multiplication
    return x

'''
Finally, print the answer for the given n and a

It should take a couple minutes to run
'''
print(smallest2toNDivsMod(500500, 500500507))