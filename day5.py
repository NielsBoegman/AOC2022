import sys
import copy
crane = [[] for i in range(9)]
commands = []
for _ in range(8):
    boxes = input()
    for x in range(1,10):
        if boxes[x+((x-1)*3)] == ' ':
            continue
        else: crane[x-1].append(boxes[x+((x-1)*3)])
trash = input()
trash = input()
for line in sys.stdin:
    temp = line.split()
    com = []
    for x in range(1,6,2):
        com.append(int(temp[x]))
    commands.append(com)
crane2 = copy.deepcopy(crane)

def part1():
    for comm in commands:
        for _ in range(1,comm[0]+1):
            crane[comm[2]-1].insert(0, crane[comm[1]-1][0])
            crane[comm[1]-1].pop(0)
    result = ""
    for x in crane:
        if not len(x) == 0:
            result += x[0]
    return result

def part2():
    for comm in commands:
        for x in range(comm[0]-1, -1, -1):
            crane2[comm[2]-1].insert(0, crane2[comm[1]-1][x])
            crane2[comm[1]-1].pop(x)
    result = ""
    for x in crane2:
        if not len(x)==0:
            result+=x[0]
    return result

print("Part1: ", part1(), "Part 2:", part2())
