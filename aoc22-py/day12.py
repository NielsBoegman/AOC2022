from dataclasses import dataclass
from typing import List
from typing import Tuple

@dataclass
class Coordinate:
    position: Tuple[int,int]
    value: int
    parent: 'Coordinate'

file = open("day12.txt")
lines = file.readlines()
field = []
queue = []
final = Coordinate("","","")
for y in range(len(lines)):
    temp = []
    line = lines[y].strip("\n")
    for x in range(len(line)):
        if line[x] == 'S':
            temp.append([ord('a'),True])
            queue.append(Coordinate((y,x),ord('a'),""))
        elif line[x] == 'E':
            temp.append([ord('z')+1, False])
        elif line[x] == 'a': #Comment for part 1
            temp.append([ord('a'),True])
            queue.append(Coordinate((y,x),ord('a'),""))
        else:
            temp.append([ord(line[x]),False])
    field.append(temp[:])
while len(queue) != 0:
    current = queue.pop(0)
    #print(len(queue), "-len ", current.position, "-pos ", chr(current.value))
    if current.value == ord('z')+1:
        final = current
        break
    if not current.position[0]+1 >= len(field):
        #print(field[current.position[0]+1][current.position[1]])
        if (field[current.position[0]+1][current.position[1]][0] - current.value <= 1 or (current.value == ord('y') and field[current.position[0]+1][current.position[1]][0] == ord('z')+1)) and not field[current.position[0]+1][current.position[1]][1]:
            queue.append(Coordinate((current.position[0]+1,current.position[1]),field[current.position[0]+1][current.position[1]][0], current))
            field[current.position[0]+1][current.position[1]][1]=True
    if not current.position[0]-1 < 0:
        #print(field[current.position[0]-1][current.position[1]])
        if (field[current.position[0]-1][current.position[1]][0] - current.value <= 1 or (current.value == ord('y') and field[current.position[0]-1][current.position[1]][0] == ord('z')+1)) and not field[current.position[0]-1][current.position[1]][1]:
            queue.append(Coordinate((current.position[0]-1,current.position[1]),field[current.position[0]-1][current.position[1]][0], current))
            field[current.position[0]-1][current.position[1]][1]=True
    if not current.position[1]+1 >= len(field[0]):
        #print(field[current.position[0]][current.position[1]+1])
        if (field[current.position[0]][current.position[1]+1][0] - current.value<=1 or (current.value == ord('y') and field[current.position[0]][current.position[1]+1][0] == ord('z')+1)) and not field[current.position[0]][current.position[1]+1][1]:
            queue.append(Coordinate((current.position[0],current.position[1]+1),field[current.position[0]][current.position[1]+1][0], current))
            field[current.position[0]][current.position[1]+1][1]=True
    if not current.position[1]-1<0:
        #print(field[current.position[0]][current.position[1]-1])
        if (field[current.position[0]][current.position[1]-1][0] - current.value<=1 or (current.value == ord('y') and field[current.position[0]][current.position[1]-1][0] == ord('z')+1))and not field[current.position[0]][current.position[1]-1][1]:
            queue.append(Coordinate((current.position[0],current.position[1]-1),field[current.position[0]][current.position[1]-1][0], current))
            field[current.position[0]][current.position[1]-1][1]=True
part1 = 0
while not final.parent == "":
    #print(final.position)
    part1+=1
    final = final.parent

print("Part1: ", part1)