
class Set:
	def __init__(self):
		self.map = {}

	def adjoin(self, item):
		if self.map.has_key(item):
			return False
		self.map[item] = True
		return True

	def delete(self, item):
		if not self.map.has_key(item):
			return None
		return self.map.pop(item)

	def member(self, item):
		return self.map.has_key(item)

	def to_list(self):
		return self.map.keys()

	def intersection(self, other):
		result = Set()
		for item in other.map.keys():
			if self.map.has_key(item):
				result.adjoin(item)
		return result

	def union(self, other):
		d = {}
		d.update(self.map)
		d.update(other.map)
		return self.__make_new_set(d)

	def difference(self, other):
		result = Set()
		for item in other.map:
			if not self.map.has_key(item):
				result.adjoin(item)
		for item in self.map:
			if not other.map.has_key(item):
				result.adjoin(item)
		return result

	def size(self):
		return len(self.map)

	def __make_new_set(self, d):
		result = Set()
		for item in d:
			result.adjoin(item)
		return result

	def __str__(self):
		return '(' + ','.join([str(i) for i in self.map.keys()]) + ')'

s = Set()
s.adjoin(5)
s.adjoin(4)
s.adjoin(5)
s.adjoin(3)
print s

s.delete(5)
print s

print s.member(2)
print s.member(4)

s2 = Set()
s2.adjoin(4)
s2.adjoin(1)
s2.adjoin(5)
print s, s2, s.intersection(s2)
print s, s2, s.union(s2)
print s, s2, s.difference(s2)