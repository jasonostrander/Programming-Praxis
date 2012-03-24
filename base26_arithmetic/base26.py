
def from_b26(s):
    s = s.upper()
    first = ord('A')

    n = 0
    r = 1
    for ch in s[::-1]:
        n += (ord(ch) - first)*r
        r *= 26

    return n

def to_b26(n):
    first = ord('A')
    s = ''
    r = 26
    while n:
        x = n % r
        n /= r
        s += chr(x + first)
    return s[::-1]

def mult(a,b):
    return to_b26(from_b26(a) * from_b26(b))

print from_b26('CBA')
print to_b26(26)
print mult('CSGHJ', 'CBA')
