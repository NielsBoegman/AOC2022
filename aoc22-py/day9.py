import sys
rope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
#rope=[(0,0),(0,0)]
allcoords=[]
allcoords.append((0,0))
movementdict = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
}

def moveTail(head, tail):
    if abs(head[0]-tail[0]) >1 and abs(head[1]-tail[1]) >1:
        x = tail[0]+(head[0]-tail[0])//2
        y = tail[1]+(head[1]-tail[1])//2
        tail = (x,y)
    elif head[0]-tail[0] > 1:
        tail = (tail[0]+1,head[1])
    elif head[0]-tail[0]<-1:
        tail=(tail[0]-1,head[1])
    elif head[1]-tail[1] > 1:
        tail=(head[0],tail[1]+1)
    elif head[1]-tail[1] <1:
        tail = (head[0],tail[1]-1)
    return tail

for line in sys.stdin:
    data = line.split()
    if not len(data) == 0:
        for x in range(int(data[1])):
            rope[0] = (rope[0][0]+movementdict[data[0]][0],rope[0][1]+movementdict[data[0]][1])
            for x in range(1,len(rope)):
                if (abs(rope[x][0]-rope[x-1][0])>1 or abs(rope[x][1]-rope[x-1][1])>1):
                    rope[x] = moveTail(rope[x-1],rope[x])
            allcoords.append(rope[len(rope)-1])

part1 = len(set(allcoords))
print("Part1: ", part1)