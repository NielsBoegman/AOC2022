from dataclasses import dataclass
from typing import List
import sys

@dataclass
class Dir:
    name: str
    dirs: List['Dir']
    size: int
    parent: 'Dir'

root = Dir('/', [],0,"")
current = root
for line in sys.stdin:
    data = line.split()
    if line == "$ cd /\n":
        continue
    elif data[0] == '$':
        if data[1] == "ls":
            continue
        elif data[1] == "cd":
            if not data[2] == "..":
                for i in range(len(current.dirs)):
                    if current.dirs[i].name == data[2]:
                        current = current.dirs[i]
            else: current = current.parent
    elif data[0] == "dir":
        current.dirs.append(Dir(data[1],[],0,current))
    else:
        current.size += int(data[0])
print(root)