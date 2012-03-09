
class SparseSet():
    def __init__(self, u):
        self.n = 0
        self.D = [None] * u
        self.S = [None] * u

    def insert(self, k):
        self.D[self.n] = k
        self.S[k] = self.n
        self.n += 1

    def lookup(self, k):
        return self.S[k] < self.n and self.D[self.S[k]] == k

    def iterate(self):
        for i in range(self.n):
            yield self.D[i]
        
    def clear(self):
        self.n = 0

    def __str__(self):
        s = 'n = %d\n' % (self.n)
        s += 'D = ' + str(self.D)
        s += '\n'
        s += 'S = ' + str(self.S)
        return s


s = SparseSet(10)
s.insert(9)
s.insert(2)
s.insert(3)
try:
    s.insert(20)
except:
    print 'invalid insert failed ;-)'
print s
print [i for i in s.iterate()]

print s.lookup(9)
s.clear()
print s.lookup(9)
print s
