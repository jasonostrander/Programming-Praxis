import sys
import itertools as it

def brute(x):
    a = tuple(str(x))
    li = [int(''.join(elem)) for elem in it.dropwhile(lambda i: int(''.join(i)) <= x, it.permutations(sorted(a)))]
    return li[0]

def swap(x):
    a = list(str(x))
    f = 0
    g = 0
    for k in range(len(a)-1):
        if a[k] < a[k+1]:
            f = k
    for l in range(len(a)):
        if a[f] < a[l]:
            g = l
    a[f],a[g] = a[g],a[f]
    li = [e for e in it.chain(a[:f+1], a[f+1:][::-1])]
    return int(''.join(li))

x = int(sys.argv[1])    
print brute(x)
print swap(x)
