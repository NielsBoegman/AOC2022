import sys
#Part1
def objectScore(round):
    match round:
        case [_,'X']:
            return 1
        case [_,'Y']:
            return 2
        case [_,'Z']:
            return 3

def detectWin(round):
    match round:
        case ['A','X']:
            return 0+3
        case ['A','Y']:
            return 3+1
        case ['A','Z']:
            return 6+2
        case ['B','X']:
            return 0+1
        case ['B','Y']:
            return 3+2
        case ['B','Z']:
            return 6+3
        case ['C','X']:
            return 0+2
        case ['C','Y']:
            return 3+3
        case ['C', 'Z']:
            return 6+1

game = []
for line in sys.stdin:
    game.append(line.split())
score =0
for round in game:
    score += detectWin(round)
print(score)