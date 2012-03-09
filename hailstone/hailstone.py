def gen(x):
    n = x
    while True:
        yield n
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1

def rfind(li, value):
    for i,v in enumerate(li[::-1]):
        if v == value:
            return len(li) - 1 - i
    # should never happen
    raise Exception()

def find(func):
    li = []
    n = func.next()
    while n > 1:
        n = func.next()
        li.append(n)
    n = func.next()
    return li[rfind(li, n):]

f = gen(1000000)
print find(f)
