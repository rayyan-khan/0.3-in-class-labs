# in this version I found a labeling such that no labels were repeated
# within the "constraints", which I thought were the surrounding indexes
# and the index itself -- like a sub-triangle thing

startPzl = 'A' + '.' * 19
indexes = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
setOfChoices = {'A', 'B', 'C', 'D', 'E'}#, 'F', 'G', 'H', 'I', 'J'}
constraints = {0: {0, 1, 10, 19},
               1: {1, 0, 2, 8},
               2: {2, 1, 3, 6},
               3: {3, 2, 4, 19},
               4: {4, 3, 5, 17},
               5: {5, 4, 6, 15},
               6: {6, 1, 3, 6},
               7: {7, 6, 8, 14},
               8: {8, 1, 7, 9},
               9: {9, 8, 10, 13},
               10: {10, 9, 11, 0},
               11: {11, 10, 12, 18},
               12: {12, 11, 13, 16},
               13: {13, 9, 12, 14},
               14: {14, 7, 13, 15},
               15: {15, 5, 14, 16},
               16: {16, 12, 15, 17},
               17: {17, 4, 16, 18},
               18: {18, 11, 17, 19},
               19: {19, 0, 3, 18}}


def canAdd(pzl, choice, placementIndex):
    #print(pzl, choice, placementIndex)
    #print(constraints[placementIndex])
    #print(pzl)
    for nbrInd in constraints[placementIndex]:
        #print('nbrIndval', pzl[nbrInd])
        if choice == pzl[nbrInd]:
            return False
    return True

def isInvalid(pzl):
    for constraint in constraints: # check each constraint
        seen = set() # to store symbols seen in each constraint
        for index in constraints[constraint]: # for each index in a constraint
            sym = pzl[index] # symbol at each index
            if sym == '.': continue
            if sym in seen: # if it has been seen in the constraint
                return True # return True because its invalid
            seen.add(sym)
    return False

def solve(pzl):
    #print(pzl)
    if isInvalid(pzl):
        #print(pzl, 'invalid')
        return ''
    if '.' not in pzl:
        return pzl

    nextOpenIndex = pzl.find('.')
    chooseFrom = setOfChoices - {pzl[sym] for sym in constraints[nextOpenIndex]}
    #print(setOfChoices - {pzl[sym] for sym in constraints[nextOpenIndex]})
    for choice in chooseFrom:
        subPzl = pzl[0:nextOpenIndex] + choice + pzl[nextOpenIndex + 1:]
        result = solve(subPzl)
        if result != '':
            return result

    return ''  # failure

print('result', solve(startPzl))