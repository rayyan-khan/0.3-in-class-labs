
# find largest independent set in icosahedron where no two share a common edge

indexes = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
constraints = {0: {1, 10, 19},
               1: {0, 2, 8},
               2: {1, 3, 6},
               3: {2, 4, 19},
               4: {3, 5, 17},
               5: {4, 6, 15},
               6: {1, 3, 6},
               7: {6, 8, 14},
               8: {1, 7, 9},
               9: {8, 10, 13},
               10: {9, 11, 0},
               11: {10, 12, 18},
               12: {11, 13, 16},
               13: {9, 12, 14},
               14: {7, 13, 15},
               15: {5, 14, 16},
               16: {12, 15, 17},
               17: {4, 16, 18},
               18: {11, 17, 19},
               19: {0, 3, 18}}

def updateChoices(choices, choice):
    return {chc for chc in choices if chc not in constraints[choice] and chc != choice}

def solve(indepSet, choices):
    if not choices:
        return indepSet

    for choice in choices:
        newIndepSet = {index for index in indepSet}
        newIndepSet.add(choice)
        newChoices = updateChoices(choices, choice)
        result = solve(newIndepSet, newChoices)
        if result:
            return result

    return False

startSet = set()
print(solve(startSet, indexes))