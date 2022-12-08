import sys
forest = []
bos = []
for line in sys.stdin:
    line = line.strip()
    if not len(line) == 0:
        forest.append([[int(x),False ]for x in line])
        bos.append([[int(x),1] for x in line])

def setEdges():
    for y in range(len(forest)):
        forest[0][y][1] = True
        bos[0][y][1] = 0
        forest[len(forest)-1][y][1] = True
        bos[len(bos)-1][y][1] = 0
    for x in range(len(forest[1])):
        forest[x][0][1] = True
        bos[x][0][1]=0
        forest[x][len(forest[1])-1][1] = True
        bos[x][len(bos)-1][1]=0

def checkTree(x,y):
    checks = [True,True,True,True]
    for z in range(x):
        if forest[z][y] >= forest[x][y]:
            checks[0] = False
            break
    for z in range(len(forest[x])-1,x,-1):
        if forest[z][y] >= forest[x][y]:
            checks[1] = False
            break
    for z in range(y):
        if forest[x][z] >= forest[x][y]:
            checks[2] = False
            break
    for z in range(len(forest)-1,y,-1):
        if forest[x][z] >= forest[x][y]:
            checks[3] = False
            break
    res = False
    for x in checks:
        res = res or x
    return res

def checkTreeBos(x,y):
    res = []
    for z in range(x-1,-1,-1):
        if z == 0:
            res.append(x)
        elif bos[z][y][0] >= bos[x][y][0]:
            res.append(x-z)
            break
    for z in range(x+1,len(bos[0])):
        if z == len(bos[0])-1:
            res.append(z-x)
        elif bos[z][y][0] >= bos[x][y][0]:
            res.append(z-x)
            break
    for z in range(y-1,-1,-1):
        if z == 0:
            res.append(y)
        elif bos[x][z][0] >= bos[x][y][0]:
            res.append(y-z)
            break
    for z in range(y+1,len(bos)):
        if z == len(bos)-1:
            res.append(z-y)
        elif bos[x][z][0] >= bos[x][y][0]:
            res.append(z-y)
            break
    final = 1
    for z in res:
        final *= z
    return final

def setMiddle():
    for x in range(1,len(forest[1])-1):
        for y in range(1,len(forest)-1):
            forest[x][y][1] = checkTree(x,y)
            bos[x][y][1] = checkTreeBos(x,y)


def part1():
    count=0
    for x in range(len(forest[1])):
        for y in range(len(forest)):
            if forest[x][y][1]:
                count+=1
    return count

def part2():
    maximum=0
    for x in range(len(bos[0])):
        for y in range(len(bos)):
            maximum = max(maximum, bos[x][y][1])
    return maximum
    
setEdges()
setMiddle()
print("Part1: ", part1(), "Part2: ", part2())