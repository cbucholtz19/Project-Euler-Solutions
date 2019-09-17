def is_prime(n): #The classic is_prime function returns again
    if (n>1):
        for d in range(2, int(n**(0.5))+1):
            if (n%d==0):
                return False
        return True
    return False

s = 0 #s is our sum

for x in range(2000000): #iterate through all numbers below 2mil
    if (is_prime(x)):
        s += x #if its prime, add to sum
        
print(s)