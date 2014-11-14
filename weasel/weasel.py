import string
import random

EXP = 'METHINKS IT IS LIKE A WEASEL'
CHARSET = string.ascii_uppercase + ' '

def pick():
    return CHARSET[random.randrange(0, len(CHARSET))]

def mutate(li):
    if random.random() < 0.05:
        li[random.randrange(0, len(li))] = pick()

def score(li):
    result = 0
    for i in range(len(li)):
        if li[i] == EXP[i]:
            result = result + 1
    return result

# start with random string
curr = [pick() for i in range(28)]
winner = curr
top_score = 0
iters = 0
while top_score < len(winner):
    # Make 100 copies
    copies = [list(winner) for i in range(100)]
    for li in copies:
        mutate(li)
        s = score(li)
        if  s > top_score:
            winner = li
            top_score = s
    iters = iters + 1
    print str(iters) + ': ', ''.join(winner), top_score
