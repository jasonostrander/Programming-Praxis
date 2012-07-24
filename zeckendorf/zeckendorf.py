import sys

n = int(sys.argv[1])

def fib(x):
	n = 1
	m = 1
	while n < x:
		yield n
		n, m = m, m+n

def drop_after(li, x):
	for i, n in enumerate(li):
		if n > x:
			return li[:i]
	return list(li)

def zeck(n):
	d = [x for x in fib(n)]

	result = []
	while n:
		result.append(d[-1])
		n = n - d[-1]
		d = drop_after(d, n)

	return result

result = zeck(n)
print result, '=', sum(result)
