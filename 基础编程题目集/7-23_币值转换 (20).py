unit = {
    1: 'S',
    2: 'B',
    3: 'Q',
    4: 'W',
    5: 'S',
    6: 'B',
    7: 'Q',
    8: 'Y'
}
trans = lambda x: chr(x+ord('a'))
n = raw_input()

r = ''
isZero = False
for index, value in enumerate(n):
    value = int(value)
    uPos = len(n) - index - 1
    if value == 0:
        isZero = True
        if not (len(n) == 9 and n[1:] == '00000000') and uPos == 4:
            r += unit[uPos]
            isZero = False
    else:
        if isZero:
            r += trans(0)
        r += trans(value)
        if uPos in unit:
            r += unit[uPos]
        isZero = False

if isZero and len(n) == 1:
    r = trans(0)

print r
