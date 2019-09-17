'''
Created by Conrad Bucholtz, 9/19/2018

Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.



-----MY SOLUTION-----

First, build functions that will check if a number is a multiple of 3 or 5
'''

def multOf3(n):
    if (n%3 == 0):
        return True
    return False

def multOf5(n):
    if (n%5 == 0):
        return True
    return False

'''
sumOfMults3_5Below(n) will sum all the numbers below n that are multiples
of either 3 or 5
'''

def sumOfMults3_5Below(n):
    x = 0;
    for i in range(1, n): #does not include n
        if (multOf3(i) or multOf5(i)):
            x += i
    return x

'''
Finally, print the answer to the problem where n=1000
'''

print(sumOfMults3_5Below(1000))