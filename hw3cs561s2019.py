import copy

def getOptimalMoves(gridBoard):
    simulateBoard = [[0 for x in range(N)] for x in range(N)]
    optimalPolicyMatrix = [['' for y in range(N)] for y in range(N)]
    while simulateBoard != gridBoard:
        simulateBoard = copy.deepcopy(gridBoard)
        for i in range(0, N):
            for j in range(0, N):
                maxRewardValue = float("-inf")
                # Check for wall or terminal
                if gridBoard[i][j] == float("-inf") or terminalMatrix[i][j] == "T":
                    if gridBoard[i][j] == float("-inf"):
                        optimalPolicyMatrix[i][j] = "N"
                    else:
                        optimalPolicyMatrix[i][j] = "E"
                # If neither wall nor terminal
                else:
                    #Up
                    if i - 1 >= 0 and gridBoard[i - 1][j] != float("-inf"):
                        value1 = 0.0
                        value2 = 0.0
                        if j - 1 >= 0:
                            if gridBoard[i - 1][j - 1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i - 1][j - 1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if j + 1 <= N - 1:
                            if gridBoard[i - 1][j + 1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i - 1][j + 1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 =  ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i - 1][j] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "U"
                    else:
                        value1 = 0.0
                        value2 = 0.0
                        if j - 1 >= 0:
                            if i-1 >= 0 and gridBoard[i - 1][j - 1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i - 1][j - 1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 =  ((1 - float(P)) * gridBoard[i][j]) / 2
                        if j + 1 <= N - 1:
                            if i-1 >= 0 and gridBoard[i - 1][j + 1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i - 1][j + 1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i][j] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "U"
                    #Down
                    if i + 1 <= N - 1 and gridBoard[i + 1][j] != float("-inf"):
                        value1 = 0.0
                        value2 = 0.0
                        if j - 1 >= 0:
                            if gridBoard[i+1][j - 1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i+1][j - 1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if j + 1 <= N - 1:
                            if gridBoard[i+1][j + 1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i+1][j + 1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i + 1][j] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "D"
                    else:
                        value1 = 0.0
                        value2 = 0.0
                        if j - 1 >= 0:
                            if i + 1 <= N - 1 and gridBoard[i+1][j - 1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i+1][j - 1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if j + 1 <= N - 1:
                            if i + 1 <= N - 1 and gridBoard[i+1][j + 1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i+1][j + 1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i][j] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "D"
                    #Left
                    if j - 1 >= 0 and gridBoard[i][j - 1] != float("-inf"):
                        value1 = 0.0
                        value2 = 0.0
                        if i + 1 <= N - 1:
                            if gridBoard[i + 1][j-1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i + 1][j-1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if i - 1 >= 0:
                            if gridBoard[i - 1][j-1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i - 1][j-1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i][j - 1] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "L"
                    else:
                        value1 = 0.0
                        value2 = 0.0
                        if i + 1 <= N - 1:
                            if j-1 >=0 and gridBoard[i + 1][j-1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i + 1][j-1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if i - 1 >= 0:
                            if j-1 >= 0 and gridBoard[i - 1][j-1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i - 1][j-1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i][j] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "L"
                    #Right
                    if j + 1 <= N - 1 and gridBoard[i][j + 1] != float("-inf"):
                        value1 = 0.0
                        value2 = 0.0
                        if i + 1 <= N - 1:
                            if gridBoard[i + 1][j+1] != float("-inf"):
                                value1 = ((1 - float(P)) * gridBoard[i + 1][j+1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if i - 1 >= 0:
                            if j+1 >=0 and gridBoard[i - 1][j+1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i - 1][j+1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i][j + 1] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "R"
                    else:
                        value1 = 0.0
                        value2 = 0.0
                        if i + 1 <= N - 1:
                            if j+1 <= N - 1 and gridBoard[i + 1][j+1] != float("-inf") :
                                value1 = ((1 - float(P)) * gridBoard[i + 1][j+1]) / 2
                            else:
                                value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value1 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        if i - 1 >= 0:
                            if j+1 <= N -1 and gridBoard[i - 1][j+1] != float("-inf"):
                                value2 = ((1 - float(P)) * gridBoard[i - 1][j+1]) / 2
                            else:
                                value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        else:
                            value2 = ((1 - float(P)) * gridBoard[i][j]) / 2
                        rewardValue = float(Rp) + (float(discountFactor) * (float(P) * gridBoard[i][j] + value1 + value2))
                        if rewardValue > maxRewardValue:
                            maxRewardValue = rewardValue
                            optimalPolicyMatrix[i][j] = "R"
                    gridBoard[i][j] = maxRewardValue
    return optimalPolicyMatrix

#reading input
f = open("input.txt")
lines = f.readlines()
N = int(lines[0].strip('\n').strip('\r'))
W = int(lines[1].strip('\n').strip('\r'))
walls = []
for i in range(0, W):
     walls.append(lines[i+2].replace("\n", "").split(","))
T = int(lines[W+2].strip('\n').strip('\r'))
terminalStates = []
for j in range(0,T):
     terminalStates.append(lines[W+j+3].replace("\n", "").split(","))
P = lines[T+W+3].strip('\n').strip('\r')
Rp = lines[T+W+4].strip('\n').strip('\r')
discountFactor = lines[T+W+5].strip('\n').strip('\r')


gridBoard = [[0.0 for x in range(N)] for y in range(N)]
terminalMatrix = [['' for x in range(N)] for y in range(N)]

#Walls
for i in range(N-1,-1,-1):
    for j in range(0,N,1):
        for k in range(0,W,1):
            if i==int(walls[k][0])-1 and j==int(walls[k][1])-1:
                gridBoard[i][j] = float("-inf")


#Terminals
for i in range(N-1,-1,-1):
    for j in range(0,N,1):
        for k in range(0,T,1):
            if i == int(terminalStates[k][0]) - 1 and j == int(terminalStates[k][1]) - 1:
                gridBoard[i][j] = float(terminalStates[k][2])
                terminalMatrix[i][j] = "T"

solution = getOptimalMoves(gridBoard)

#returning output
o = open("output.txt", "w")
for i in range(0, N, 1):
    for j in range(0, N, 1):
        o.write(solution[i][j])
        if j != N - 1:
            o.write(",")
    o.write("\n")

