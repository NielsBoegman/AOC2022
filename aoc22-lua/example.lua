local store = { {} }
local storec = { {} }
local count = 1
local gamma = 0
local epsilon = 0
local oxygen = {}
local co2 = {}




while true do
    local temp = io.read()
    if temp == "" or temp == nil then break end
    for match in string.gmatch(temp, "%w") do
        if store[count] == nil then store[count] = {} end
        table.insert(store[count], tonumber(match))
    end
    count = count + 1
end
storec = store
local ocount = 1
while #store ~= 2 do
    local temp = { {} }
    local onecount = 0
    for j = 1, #store do
        if store[j][ocount] == 1 then onecount = onecount + 1 end
    end
    if onecount >= (#store - 1) / 2 then oxygen[ocount] = 1 else oxygen[ocount] = 0 end
    for j = 1, #store do
        if store[j][ocount] == oxygen[ocount] then
            --print(ocount,":", #store, ";", store[j][1], store[j][2], store[j][3], store[j][4], store[j][5])
            table.insert(temp, store[j])
        end
    end
    --print(tempo[1][1], tempo[1][2], tempo[1][3], tempo[1][4], tempo[1][5])
    --if(#temp == 2) then print("second=", temp[2][1], temp[2][2], temp[2][3], temp[2][4], temp[2][5])end
    ocount = ocount + 1
    store = temp
end
for i = 1, #store[2] do
    gamma = gamma + store[2][i] * 2 ^ (#store[2] - i)
end
local ccount = 1
while #storec ~= 2 do
    local temp = { {} }
    local onecount = 0
    for j = 1, #storec do
        if storec[j][ccount] == 1 then onecount = onecount + 1 end
    end
    if onecount < (#storec - 1) / 2 then co2[ccount] = 1 else co2[ccount] = 0 end
    for j = 1, #storec do
        if storec[j][ccount] == co2[ccount] then
            --print(ocount,":", #store, ";", store[j][1], store[j][2], store[j][3], store[j][4], store[j][5])
            table.insert(temp, storec[j])
        end
    end
    --print(temp[1][1], temp[1][2], temp[1][3], temp[1][4], temp[1][5])
    --if(#temp == 2) then print("second=", temp[2][1], temp[2][2], temp[2][3], temp[2][4], temp[2][5])end
    ccount = ccount + 1
    storec = temp
end
for i = 1, #storec[2] do
    epsilon = epsilon + storec[2][i] * 2 ^ (#storec[2] - i)
end
print("oxygen:", gamma, "co2:", epsilon, "total:", gamma * epsilon)
