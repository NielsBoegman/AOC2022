data = input()

def checkChars(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]==s[j]):
                return False
    return True

def part1():
    for x in range(3, len(data)):
        if checkChars(data[x-3]+data[x-2]+data[x-1]+data[x]):
            return x+1
        else: continue

def part2():
    for x in range(13, len(data)):
        temp = ""
        for y in range(x-13,x+1):
            temp += data[y]
        if(checkChars(temp)):
            return y+1
print("Part1: ", part1(), "Part2: ", part2())