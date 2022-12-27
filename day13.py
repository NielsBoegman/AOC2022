from functools import cmp_to_key
file = open("day13.txt")
lines = file.readlines()
x=[]
y=[]
inputs=[]
count=0
inputs2=[]
for i in range(0,len(lines),3):
    x = eval(lines[i])
    y = eval(lines[i+1])
    inputs2.append(x)
    inputs2.append(y)
    inputs.append((x,y))
inputs2.append([[2]])
inputs2.append([[6]])
            
def compare(left,right):
    result = 0
    if isinstance(left,list):
        if isinstance(right,list):
            for i in range(min(len(left),len(right))):
                result = compare(left[i],right[i])
                if  result == 0:
                    continue
                else: return result
            if result == 0:
                if len(left) > len(right):
                    result = -1
                elif len(left) < len(right):
                    result = 1
            return result
        else:
            return compare(left, [right])
    
    else:
        if isinstance(right,list):
            return compare([left], right)
        else:
            if left > right:
                return -1
            elif left < right:
                return 1
            else:
                return 0

def part1():
    final = 0
    for i in range(len(inputs)):
        if compare(inputs[i][0], inputs[i][1]) == 1:
            final +=(i+1)
    return final

def part2():
    sorted_list = sorted(inputs2, key=cmp_to_key(compare), reverse=True)
    print(sorted_list)
    one = 0
    two = 0
    for x in range(len(sorted_list)):
        if sorted_list[x] == [[2]]:
            one = x+1
        if sorted_list[x] == [[6]]:
            two = x+1
    return one*two
        

#print("Part1: ", part1())
print(part2())