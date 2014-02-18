li = [1,2,3]
li2 = [3,1,2, 4,5]

def uniq(li, li2):
    d = {}
    for i in li:
        d[i] = True
    result = []
    for i in li2:
        if not d.has_key(i):
            result.append(i)
    return result
            
result = uniq(li, li2)
print result
assert(result == [4,5])

