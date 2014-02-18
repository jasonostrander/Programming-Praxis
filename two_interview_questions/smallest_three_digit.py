import sys

def smallest(n):
    def prod(x):
        return reduce(lambda x,y: x*y, [int(ch) for ch in str(x)])
    if n > 9*9*9: return None
    
    for x in range(111, 1000):
        t = prod(x)
        if t == n:
            return x
    return None

assert(smallest(100) == 455)
print smallest(int(sys.argv[1]))
