cache = {}

def latticePaths(x, y):
    if ((x,y) in cache):
        return cache[(x,y)]
    if (x==1 or y==1):
        paths = 1
        cache[(x,y)] = paths
        return paths
    paths = latticePaths(x-1, y) + latticePaths(x, y-1)
    cache[(x,y)] = paths
    return paths

print(latticePaths(21,21))

'''
YAY FOR MEMOIZATION!!!
'''