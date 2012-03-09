
def sum_list(li, exp):
    l = len(li)
    for i in range(l):
        for j in range(i+1, l):
            if li[i] + li[j] == exp:
                return (li[i], li[j])
    return ()

li = [1,4,6,2,7,8]

result = sum_list(li, 5)
assert(result == (1,4))

result = sum_list(li, 10)
assert(result == (4,6))

result = sum_list(li, 9)
assert(result == (1,8))

result = sum_list(li, 100)
assert(result == ())
