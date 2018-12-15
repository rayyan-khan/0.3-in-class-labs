import time

startPuzzle = [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]

def findHoles(puzzle): # list of indexes that are holes -- also everything else is therefore peg
    holes=[]
    for k in range(25):
        if puzzle[k] == 0 and k not in (0, 4, 20, 24):
            holes.append(k)
    return holes

def neighbors(puzzle):
    # index is index of hole, [[possible jump location, what you jump over],[possible jump location, etc]]
    lookup = [
        [],
        [(3, 2), (13, 7), (11, 6)],
        [(14, 8), (12, 7)],
        [(1, 2), (13, 8)],
        [],
        [(7, 6), (17, 11), (15, 10)],
        [(8, 7), (18, 12), (16, 11)],
        [(5, 6), (9, 8), (19, 13)],
        [(6, 7), (18, 13)],
        [(7, 8), (19, 14)],
        [(12, 11), (22, 16)],
        [(1, 6), (13, 12), (23, 17), (21, 16)],
        [(2, 7), (10, 11), (14, 13), (22, 17)],
        [(3, 8), (23, 18), (11, 12), (1, 7)],
        [(12, 13), (2, 8)],
        [(5, 10), (17, 16)],
        [(6, 11), (18, 17)],
        [(15, 16), (5, 11), (7, 12), (19, 18)],
        [(8, 13), (6, 12), (16, 17)],
        [(17, 18), (7, 13), (9, 14)],
        [],
        [(11, 16), (23, 22)],
        [(12, 17), (10, 16)],
        [(11, 17), (13, 18), (21, 22)],
        []
    ]

    # dict of indexes and their levels
    dictLev = {1: 1, 2: 1, 3: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 3,
               14: 3, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 21: 5, 22: 5, 23:5}

    # notes: number of holes can vary unlike slider
    holes = findHoles(puzzle)
    nbrList = []

    #for every hole if lookup[hole index] is not 0 in the string AND the peg in between them not empty
    #then lookup[hole index][1] can be jumped over from lookup[hole index][0] into puzzle[hole index]

    for index in holes:
        #find all the neighbors for each hole
        for n in range(len(lookup[index])):
            move = str(lookup[index][n][1])
            if puzzle[lookup[index][n][0]] and puzzle[lookup[index][n][1]]:
                #nbr list append puzzle made by doing that
                copy = puzzle.copy()
                copy[index] = 1
                copy[lookup[index][n][0]] = 0
                copy[lookup[index][n][1]] = 0

                # move types (marbles): if abs(indexFrom - indexOver) == 5, then V
                # if abs(indexFrom - indexOver) == 6, then N
                # if dctLev[indexFrom] == dctLev [indexOver], then H
                if dictLev[lookup[index][n][0]] == dictLev[lookup[index][n][1]]:
                    move = move + 'H'
                else:
                    disp = abs(lookup[index][n][0]-lookup[index][n][1])
                    if disp == 5:
                        move = move + 'V'
                    else:
                        move = move + 'N'
                nbrList.append((copy,move))
    return nbrList

def solve(puzzle,goal='any'):
    parseMe=[(puzzle,'')]
    pathList=[]
    dictSeen={''.join(map(str,puzzle)):('','')} #string of puzzle:(parent,move to get there)
    #level={[0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0]:0}
    while parseMe:
        pzl = parseMe.pop(0)
        if sum(pzl[0])==1:
            if goal != 'any':
                if pzl[0].index(1) == goal:
                    key = ''.join(map(str, pzl[0]))
                    while key != '':
                        #print(key)
                        pathList.insert(0, dictSeen[key][1])
                        key = dictSeen[key][0]
                    pathList.remove('')
                    return pathList
                else:
                    for nbr in neighbors(pzl[0]):
                        nbrPzl = ''.join(map(str, nbr[0]))  # str of puzzle
                        move = nbr[1]
                        if nbrPzl not in dictSeen:
                            #level[nbrPzl] = level[pzl] + 1
                            parseMe.append(nbr)  # list puzzle,move
                            dictSeen[nbrPzl] = (
                            ''.join(map(str, pzl[0])), move)  # key = string of puzzle, value = string of parent, move
            else:
                key = ''.join(map(str, pzl[0]))
                while key!='':
                    #print(key)
                    pathList.insert(0,dictSeen[key][1])
                    key=dictSeen[key][0]
                pathList.remove('')
                return pathList
        else:
            for nbr in neighbors(pzl[0]):
                nbrPzl= ''.join(map(str,nbr[0])) #str of puzzle
                move = nbr[1]
                if nbrPzl not in dictSeen:
                    parseMe.append(nbr) #list puzzle,move
                    dictSeen[nbrPzl]=(''.join(map(str,pzl[0])),move)#key = string of puzzle, value = string of parent, move
    print(dictSeen)
    return "no solution"

start = time.time()
#print(solve(startPuzzle, 12))

print('time', time.time()-start)
