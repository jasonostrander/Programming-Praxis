def move(li):
    l = 0
    r = len(li) - 1
    while l < r:
        if li[l] == 0 and li[r] != 0:
            li[l], li[r] = li[r], li[l]
            l = l + 1
            r = r - 1
        if li[l] != 0:
            l = l + 1
        if li[r] == 0:
            r = r - 1
    return li

li = [1,0,2,0,0,3,4]
assert(move(li) == [1,4,2,3,0,0,0])

print '[]', move([])
print '[0,0,0]', move([0, 0, 0])
print '[1,2,3]', move([1,2,3])
