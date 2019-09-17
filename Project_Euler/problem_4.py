'''
Created by Conrad Bucholtz, 9/24/2018

Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.



-----MY SOLUTION-----

This program needs two functions:
    -One that will check if a number is a palindrome
    -One that will check if a number has two 3-digit factors
'''

import math

def isPalindrome(n):
    s = str(n) #it is easier to treat the number as a string
    i = 0
    while (i < math.ceil(len(s)/2)): #iterate halfway through the number
        if s[i] == s[len(s)-(i+1)]: #check equality on each side of the number
            pass
        else:
            return False #if not equal, return false
        i += 1
    return True #if loop fully executes, return true

def hasTwo3DigFacts(n):
    for i in range(100, 1000): #iterate through all 3-digit numbers
        if int(n/i) == (n/i): #if number evenly divides
            if (n/i) > 99 and (n/i) < 1000: #and if that number is also 3-digit
                #print(i, int(n/i)) #uncomment to see the factors
                return True
    return False

'''
Now, start at the largest possible solution (999*999) and iterate downwards in
order to print the first solution
'''

for x in range(998001, 0, -1):
    if isPalindrome(x) and hasTwo3DigFacts(x):
        print(x)
        break; #exit the loop
