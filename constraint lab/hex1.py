
# hexagon puzzle, a large hexagon with 24 inner triangles that also form 7 sub-hexagons
# hexagon is a string with each triangle as an index len 24
# just pretend they're numbered 1 - 24 r-l u-d
# lets say the 6 labels are A, B, C, D, E, F
# ........................ start puzzle
# inner hexagons are indexes: -- edit: these minus one bc start 0
# TL: 1, 2, 3, 7, 8, 9
# TR: 3, 4, 5, 9, 10, 11
# ML: 6, 7, 8, 13, 14, 15
# MC: 8, 9, 10, 15, 16, 17
# MR: 10, 11, 12, 17, 18, 19
# BL: 14, 15, 16, 20, 21, 22
# BR: 16, 17, 18, 22, 23, 24

startPzl = '........................'
setOfChoices = {'A', 'B', 'C', 'D', 'E', 'F'}

def copies(tpl):
    seen = set()
    for label in tpl:
        if label != '.':
            if label in seen:
                return True  # true if labels in subhex aren't unique
            else:
                seen.add(label)
    return False  # otherwise it's still valid

def checkTwoFives(pzl):
    labelCounts = {label: pzl.count(label) for label in setOfChoices}
    fiveCount = sum([1 for label in labelCounts if labelCounts[label] == 5])
    if fiveCount == 2:
        return labelCounts
    return False

def isInvalid(hexPzl):  # find out better way this isn't nice
    hexTL = (hexPzl[0], hexPzl[1], hexPzl[2], hexPzl[6], hexPzl[7], hexPzl[8])
    hexTR = (hexPzl[2], hexPzl[3], hexPzl[4], hexPzl[8], hexPzl[9], hexPzl[10])
    hexML = (hexPzl[5], hexPzl[6], hexPzl[7], hexPzl[12], hexPzl[13], hexPzl[14])
    hexMC = (hexPzl[7], hexPzl[8], hexPzl[9], hexPzl[14], hexPzl[15], hexPzl[16])
    hexMR = (hexPzl[9], hexPzl[10], hexPzl[11], hexPzl[16], hexPzl[17], hexPzl[18])
    hexBL = (hexPzl[13], hexPzl[14], hexPzl[15], hexPzl[19], hexPzl[20], hexPzl[21])
    hexBR = (hexPzl[15], hexPzl[16], hexPzl[17], hexPzl[21], hexPzl[22], hexPzl[23])

    if copies(hexTL) or copies(hexTR) or copies(hexML) \
            or copies(hexMC) or copies(hexMR) or copies(hexBL) or copies(hexBR):
        return True  # true if the overall puzzle contains a subhex with copies, meaning its invalid


def bruteForce(pzl):
    if isInvalid(pzl):
        return ''
    if '.' not in pzl:
        labelCounts = checkTwoFives(pzl)
        if labelCounts:
            print(labelCounts)
            return pzl

    nextOpenIndex = pzl.find('.')
    for choice in setOfChoices:
        subPzl = pzl[0:nextOpenIndex] + choice + pzl[nextOpenIndex + 1:]
        bf = bruteForce(subPzl)
        if bf != '':
            return bf

    return ''  # failure

print(bruteForce(startPzl))
