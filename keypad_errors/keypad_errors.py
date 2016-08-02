
def check(pin, kinput):
    if len(kinput) > len(pin):
        return False
    i = 0
    j = 0
    suspect = None
    seen = {}
    while i < len(kinput):
        if not suspect and kinput[i] != pin[j] and not seen.has_key(pin[j]):
            suspect = pin[j]
            j = j + 1
        if kinput[i] != pin[j] and pin[j] != suspect:
            return False
        seen[pin[j]] = True
        j = j + 1
        i = i + 1
    return True

def check2(pin, kinput):
    if kinput == pin:
        return True
    temp = pin
    for ch in pin:
        temp = [a for a in pin if a != ch]
        if kinput == ''.join(temp):
            return True
    return False

def test(check):
    assert(check('18684', '164'))
    assert(not check('18684', '1864'))
    assert(check('18684', '8684'))
    assert(check('18684', '1884'))
    assert(check('18684', '1868'))
    assert(not check('18684', '884'))
    assert(not check('18684', '186844'))
    assert(check('18684', '18684'))
    assert(check2('18684', '164'))

test(check)
test(check2)
