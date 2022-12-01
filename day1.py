import sys
currentelf = 0
elves = []
for line in sys.stdin:
    if not line == "\n":
        currentelf += int(line)
    else:
        elves.append(currentelf)
        currentelf=0
elves.sort()

print("\n",elves[-1] + elves[-2] + elves[-3])