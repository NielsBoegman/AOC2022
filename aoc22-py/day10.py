file = open("day10.txt")
lines = file.readlines()
sprite=1
cycles=1
def checkCycle(dat,cyc,xs):
    if((cyc-20)%40 == 0):
        return cyc * xs
    elif((cyc-20)%40==1):
        if dat[0] == "noop":
            return 0
        else:
            return (cyc-1) * (xs - int(dat[1]))
    else:
        return 0

def part1(lines):
    signal = 0
    cycle = 1
    x = 1
    for line in lines:
        data = line.split()
        if not len(data) == 0:
            if data[0] == "noop":
                cycle +=1
                signal += checkCycle(data,cycle,x)
            else:
                cycle+=2
                x += int(data[1])
                signal += checkCycle(data,cycle,x)
    return signal

def part2(lines):
    lin = 0
    sprite = 1
    toadd=0
    crt = ""
    skip = False
    for i in range(0,240):
        if (i)%40 == 0 and i >= 40:
            crt +="\n"
        if(i%40 in range(sprite-1,sprite+2)):
            crt+='#'
            # crt +=str(sprite)
            # crt +=str(i%40)
        else:
            crt+='.'
            # crt+=str(sprite)
            # crt+=str(i%40)
        if skip:
            skip = False
            sprite +=toadd
            continue
        line = lines[lin].split()
        lin+=1
        if(line[0] == "noop"):
            continue
        else:
            skip = True
            toadd = int(line[1])
    print(crt)

        
    

print("Part1: ", part1(lines),"\n")
part2(lines)