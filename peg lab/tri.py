startPuzzle = [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]

def findHoles(puzzle): #list of indexes that are holes -- also everything else is therefore peg
    holes=[]
    for k in range(15):
        if puzzle[k]==0:
            holes.append(k)
    return holes

def neighbors(puzzle):
    # index is index of hole, [[possible jump location, what you jump over],[possible jump location, etc]]
    lookup = [
                [[3, 1], [5, 2]], # if hole at 0, you can jump over 1 to get to 3
                [[6, 3], [8, 4]],
                [[7, 4], [9, 5]],
                [[10, 6], [0, 1], [12, 7], [5, 4]],
                [[11, 7], [13, 8]],
                [[0, 2], [14, 9], [12, 8], [3, 4]],
                [[1, 3], [8, 7]], [[2, 4], [9, 8]],
                [[1, 4], [6, 7]],
                [[2, 5], [7, 8]],
                [[3, 6], [12, 11]],
                [[4, 7], [13, 12]],
                [[10, 11], [3, 7], [5, 8], [14, 13]],
                [[11, 12], [4, 8]],
                [[5, 9], [12, 13]]
             ]
    #dict of indexes and their levels
    dictLev = {0:1,1:2,2:2,3:3,4:3,5:3,6:4,7:4,8:4,9:4,10:5,11:5,12:5,13:5,14:5}
    #notes: number of holes can vary unlike slider
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
                #Moves types: if abs(indexFrom-indexOver)<level of indexFrom (top = 1), then positive
                # if == level indexFrom then neg, else horizontal
                disp = abs(lookup[index][n][0]-lookup[index][n][1])
                indLev = dictLev[lookup[index][n][0]]
                if disp<indLev:
                    move = move+'P'
                elif disp==indLev:
                    move = move+'N'
                else:
                    move = move+'H'
                nbrList.append((copy,move))
    return nbrList

def solve(puzzle,goal='any'):
    parseMe=[(puzzle,'')]
    pathList=[]
    dictSeen={''.join(map(str,puzzle)):('','')} #string of puzzle:(parent,move to get there)
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
                            parseMe.append(nbr)  # list puzzle,move
                            dictSeen[nbrPzl] = (
                            ''.join(map(str, pzl[0])), move)  # key = string of puzzle, value = string of parent, move
            else:
                key = ''.join(map(str, pzl[0]))
                while key!='':
                    print(key)
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
    return "no solution"

print(solve(startPuzzle))