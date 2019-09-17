import math

def triangle(n):
    return int(((n*n)/2) + (n/2))

def numFactors(n):
    factors = 0
    for i in range(1,math.floor(math.sqrt(n))):
        if ( (n/i).is_integer() ):
            factors += 2
    if ((n/n).is_integer()):
        factors += 1
    return factors

def firstTriangleWithNFactors(n):
    test = 3500
    while(True):
        print("Testing " + str(test))
        r = numFactors(triangle(test))
        print(r)
        if (r >= n):
            return triangle(test)
        test += 1

print(firstTriangleWithNFactors(500))