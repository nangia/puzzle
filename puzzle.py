

def mul(y, incarry, multi=3):
    rawval = multi * y + incarry
    val = rawval % 10
    carry = (rawval - val)/10
    return (carry, val)


def checkval(c, b, a):
    # the numbers are cba, cba, cba
    # result is bbb
    bbb = int("%d%d%d" % (b, b, b))
    cba = int("%d%d%d" % (c, b, a))
    return 3 * cba == bbb

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if checkval(c, b, a):
                print "%d%d%d" % (c, b, a)
