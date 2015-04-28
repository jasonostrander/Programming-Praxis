
def is_anagram1(s1, s2):
    d = {}
    for c in s1:
        v = d.setdefault(c, 0) + 1
        d[c] = v
    for c in s2:
        if not d.has_key(c):
            return False
        d[c] -= 1
        if d[c] < 0:
            return False
    return True

def is_anagram2(s1, s2):
    # not very efficient
    return sorted(s1) == sorted(s2)

def is_anagram3(s1, s2):
    d1 = {}
    for c in s1:
        v = d1.setdefault(c, 0) + 1
        d1[c] = v
    d2 = {}
    for c in s2:
        v = d2.setdefault(c, 0) + 1
        d2[c] = v
    return d1 == d2

def assert_anagram(f):
    assert(f('deposit', 'dopiest'))
    assert(f('opts', 'pots'))
    assert(f('opts', 'tops'))
    assert(f('opts', 'stop'))
    assert(not f('jason', 'susan'))

assert_anagram(is_anagram1)
assert_anagram(is_anagram2)
assert_anagram(is_anagram3)
