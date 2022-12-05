import sys
stack = [[] for i in range(9)]
for _ in range(8):
    boxes = input()
    for x in range(1,10):
        if boxes[x+((x-1)*3)] == ' ':
            continue
        else: stack[x-1].append(boxes[x+((x-1)*3)])
#TODO reverse the boxes stacks
print(stack)
