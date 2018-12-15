startPuzzle = [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
newStart = [str(i) for i in startPuzzle]
print(newStart)
print(''.join(newStart))
print(list(int(i) for i in newStart))