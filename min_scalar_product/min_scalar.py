# min scalar

def min_scalar(x, y):
	return sum([a[0]*a[1] for a in zip(sorted(x), sorted(y)[::-1])])

x = (1, 3, -5)
y =  (-2, 4, 1)
print min_scalar(x,y)

x = (1,2,3,4,5)
y = (1,0,1,0,1)
print min_scalar(x,y)