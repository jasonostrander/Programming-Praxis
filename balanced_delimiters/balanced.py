import sys

isStart = lambda c: c == '(' or c == '[' or c == '{'
isEnd = lambda c: c == ')' or c == ']' or c == '}'

def match(start, end):
  if start == '(' and not end == ')':
    return False
  elif start == '[' and not end == ']':
    return False
  elif start == '{' and not end == '}':
    return False
  return True

def balanced(s):
  stack = []
  for ch in s:
    if isStart(ch):
      stack.append(ch)
    elif isEnd(ch):
      if not match(stack.pop(), ch):
        return False
  if len(stack) > 0:
    return False
  return True

assert(balanced('{}'))
assert(balanced('[]'))
assert(balanced('()'))
assert(balanced('a(b)c'))
assert(balanced('abc[d]'))
assert(balanced('a(b)c{d[e]}'))
assert(not balanced('{]'))
assert(not balanced('(]'))
assert(not balanced('a(b]c'))
assert(not balanced('abc[d}'))
assert(not balanced('a(b)c{d[e}]'))
