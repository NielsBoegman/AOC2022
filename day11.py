file = open("day11.txt")
lines = file.readlines()
monkeys = []
activity = []
divisor = []
passes = []
operations = [lambda x: x*7, lambda x: x*x, lambda x: x+8, lambda x: x+4, lambda x: x+3, lambda x: x+5, lambda x: x+7, lambda x: x*3]
monkeycount = -1
for line in lines:
    data = line.split()
    if not len(data) == 0:
        if data[0] == "Monkey":
            monkeys.append([])
            activity.append(0)
            divisor.append(0)
            passes.append([0,0])
            monkeycount+=1
            continue
        if data[0] == "Starting":
            for x in range(2,len(data)):
                data[x]=data[x].replace(',','')
                temp = int(data[x])
                monkeys[monkeycount].append(temp)
            continue
        if data[0] == "Operation:":
            continue
        if data[0] == "Test:":
            divisor[monkeycount] = int(data[3])
        if data[1] == "true:":
            passes[monkeycount][0]=int(data[5])
        if data[1] == "false:":
            passes[monkeycount][1]=int(data[5])

for i in range(20):
    for x in range(len(monkeys)):
        for item in monkeys[x]:
            activity[x]+=1
            temp = operations[x](item)
            temp = temp //3
            if temp%divisor[x] == 0:
                monkeys[passes[x][0]].append(temp)
            else:
                monkeys[passes[x][1]].append(temp)
        monkeys[x] = []
part1 = activity[-1] * activity[-2]
for x in range(len(activity)):
    activity[x] = 0

for i in range(10000):
    for x in range(len(monkeys)):
        for item in monkeys[x]:
            activity[x]+=1
            temp = operations[x](item)
            temp = temp % 9699690
            if temp%divisor[x] == 0:
                monkeys[passes[x][0]].append(temp)
            else:
                monkeys[passes[x][1]].append(temp)
        monkeys[x] = []
activity = sorted(activity)
part2 = activity[-1] * activity[-2]
print("Part1: ", part1, "Part2: ", part2)