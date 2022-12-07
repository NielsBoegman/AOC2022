from dataclasses import dataclass
from typing import List

@dataclass
class Test:
    test: List['Test']
    name: str
    parent: 'Test' =""

root = Test([],"a")
sub = Test([],"b")
temp = root
sub.parent=temp
temp.test.append(sub)
print(root)