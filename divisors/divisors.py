import sys

def divisors(n):
    d = [[] for i in range(n)]
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            d[j-1].append(i)
    return d

def find_amicable(li):
    r = []
    for i, l in enumerate(li):
        n = i + 1
        if sum(l) == 2*n:
            r.append(n)
    return r

def perfect(li, n):
    a = sum(li[n-1][:-1])
    if a >= len(li) or a == n: return None
    b = sum(li[a-1][:-1])
    return a if b == n else None

def find_perfect(li):
    s = set()
    for i, l in enumerate(li):
        n = i + 1
        p = perfect(li, n)
        if p:
            s.add(n)
    return s
li = divisors(int(sys.argv[1]))
print find_amicable(li)
print find_perfect(li)
