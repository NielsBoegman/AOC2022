import sys
score = 0
score2=0
values = []

def priority(item):
    x = ord(item)
    if x < 91:
        return x -38
    else:
        return x - 96

for line in sys.stdin:
    found = []
    values.append(line)
    for item in range(len(line)//2):
        for sitem in range(len(line)//2, len(line)):
            if line[item] == line[sitem]:
                if not line[item] in found:
                    found.append(line[item])
                    score += priority(line[item])
                else:continue
for i in range(0,len(values),3):
    for item in values[i]:
        if item in values[i+1] and item in values[i+2]:
            score2+=priority(item)
            break
print("Part1: ",score, "Part2: ", score2)