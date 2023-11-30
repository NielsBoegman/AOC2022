data = input()

def checkChars(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]==s[j]):
                return False
    return True

def part(checksize):
    for x in range(checksize, len(data)):
        temp = ""
        for y in range(x-checksize,x+1):
            temp += data[y]
        if(checkChars(temp)):
            return y+1
print("Part1: ", part(3), "Part2: ", part(13))