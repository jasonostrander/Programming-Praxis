#!/usr/bin/env python

def hailstone(n):
    collatz = lambda n: 3 * n + 1 if n & 1 else n // 2
    hs = []
    while n != 1:
        hs.append(n)
        n = collatz(n)
    hs.append(1)
    return hs

if __name__ == "__main__":
    from sys import argv
    print(hailstone(int(argv[1]) if len(argv)> 1 else 1729))
