Elves = {}
function ReadInput()
    local f = io.open("/home/pokemaster69/Documents/aoc/AOC2022/day1.txt", "r")
    local lines = f:lines()
    local count = 0
    for line in lines do
        if line == "" then
            table.insert(Elves, count)
            count = 0
        else
            local i = tonumber(line)
            if i == nil then
                break
            else
                count = count + i
            end
        end
    end
end

function Day1()
    print("Part 1: ", Elves[#Elves])
end

function Day2()
    print("Part 2: ", Elves[#Elves] + Elves[#Elves - 1] + Elves[#Elves - 2])
end

ReadInput()
table.sort(Elves)
Day1()
Day2()
