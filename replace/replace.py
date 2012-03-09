import re
from time import time

def reg_replace(s, chars):
    return re.sub('[%s]'%chars, '', s)

def replace(s, chars):
    for ch in chars:
        s = s.replace(ch, '')
    return s

def speed_test(method, s, chars):
    t0 = time()
    for i in range(10000):
        method(s, chars)
    print time() - t0
    
test = 'Programming Praxis'
print replace(test, 'aeiou')
print reg_replace(test, 'aeiou')

speed_test(replace, test, 'aeiou')
speed_test(reg_replace, test, 'aeiou')
