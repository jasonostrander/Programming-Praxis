N = 6552

def prod(a,b,c):
    return (a/100.0) * (b/100.0) * (c/100.0)
assert(prod(6300, 200, 52) == 65.52)

def wise():
    for a in range(1, N-1):
        for b in range(1, N-a-1):
            c = N - a - b; # sums to N
            if prod(a,b,c) == N/100.0:
                return [a,b,c]

print wise()
