import math, sys
from itertools import count, takewhile
 
def gen_primes():
    yield 2
    def update_composites(number,increment):
        try:
            composites[number] += [increment]
        except:
            composites[number] = [increment]
 
    composites = {4:[2]}
 
    c = count(3)
    while 1:
        next = c.next()
        #print next, composites
        smallest = min(composites.keys())
        incs = composites[smallest]
        del composites[smallest]
        for inc in incs:
            update_composites(smallest+inc,inc)
        if next < smallest:
            yield next
            c.next()
            update_composites(next**2,next)
 
g=gen_primes()
#print [g.next() for i in range(10)]

def is_perfect(n):
    primes = [p for p in takewhile(lambda p: p< math.log(n,2), gen_primes())]
    
    i = 2
    while i**2 < n:
        for e in primes:
            if i**e == n:
                return True
        i += 1
    return False

print is_perfect(int(sys.argv[1]))
