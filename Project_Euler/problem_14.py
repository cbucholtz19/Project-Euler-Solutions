

def collatzIterations(n):
    iterations = 1
    while (n != 1):
        if (n%2 == 1):
            n = (3*n) + 1
        else:
            n = int(n/2)
        iterations += 1
    return iterations


greatestIterations = 0
greatestNumber = 0
for i in range (1,1000001):
    c = collatzIterations(i)
    if (c > greatestIterations):
        greatestIterations = c
        greatestNumber = i
        
print(greatestNumber)


