import itertools

keys = '''
708894553 704488409 705674273
707478271 710167019 708093251
702013379 704030867 708691187
708374743 712748719 713581951
704387447 707015741 704308279
710872423 707947453 704996429
706323757 705031051 714623803
'''

keys = [int(i) for i in keys.strip().split()]

# uses algorithm from paxis problem: three binary algorithms
def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    if a % 2 == 0 and b % 2 == 0:
        return gcd(a >> 1, b >> 1) << 1
    if a % 2 == 0: return gcd(a >> 1, b)
    if b % 2 == 0: return gcd(a, b >> 1)
    if a > b: return gcd(a-b, b)
    else: return gcd(a, b-a)

def algo1(keys):
    result = set()
    for x,y in itertools.combinations(keys, 2):
        g = gcd(x,y)
        if g > 1:
            result.add(g)
    return list(result)

def algo2(keys):
    prod = reduce(lambda x,y: x*y, keys)

    result = set()
    for key in keys:
        g = gcd(key, (prod % key**2)/key)
        if g > 1:
            result.add(g)
    return [int(x) for x in result]

print algo1(keys)
print algo2(keys)
