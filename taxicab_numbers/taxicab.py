import sys

def get_cubes(x):
    result = []
    a,b = 1, x**1/3
    while a < b:
        n = a**3 + b**3

        if n > x:
            b -= 1
        elif n < x:
            a += 1
        elif n == x:
            result.append((a,b))
            b -= 1
    if len(result) == 2:
        return result
    return None


for i in range(100000):
    r = get_cubes(i)
    if r:
        print i, r

