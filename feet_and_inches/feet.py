
tests = map(lambda x: float(x), "0 0.2785 1.6895 11.9999 12.2785 71.9999 72 72.3492 72.9999 73 73.0135 73.0185 73.8218".split())

def to_imperial(value):
    feet = int(value/12)
    inches = int(value - feet*12)
    rem = int(round((value - feet*12 - inches)*32))

    # handle edge cases
    if rem == 32:
        inches += 1
        rem = 0
    if inches == 12:
        feet += 1
        inches = 0

    # reduce the 32nds fraction
    fract = 32
    while rem != 0 and rem % 2 == 0:
        rem = rem/2
        fract = fract/2

    result = ''
    if feet:
        result += '%d feet ' % feet
    if inches:
        result += '%d inches ' % inches
    if rem:
        result += '%d/%dth' % (rem, fract)
    return result

for test in tests:
    print to_imperial(test)
