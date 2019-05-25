class Flight:
    def __init__(self, R, M, S, O, C):
        self.R = R;
        self.M = M;
        self.S = S;
        self.O = O;
        self.C = C;
        self.L = -1;
        self.G = -1;
        self.T = -1;
def printResult(completedFlightList):
    output = open("output.txt", "w")
    for x in flights:
        output.write(str(x.L) + " " + str(x.T) + "\n")
    output.close()
    exit()
def getFlightOrder(currentFlightList, currentLandList, currentGateList, currentTakeOffList, L, G, T,
                   completedFlightList):
    if (len(currentFlightList) == 0):
        printResult(completedFlightList)
    for x in currentFlightList:
        bestTakeOffTime = -1
        bestGateTime = -1
        bestLandTime = -1
        listMinGateTime = -1
        listMinLandTime = -1
        if (T > len(currentTakeOffList)):
            bestTakeOffTime = 0
        else:
            bestTakeOffTime = min(currentTakeOffList)
        if bestTakeOffTime == 0:
            if (G > len(currentGateList)):
                bestGateTime = 0
            else:
                bestGateTime = min(currentGateList)
        else:
            minGateReachTime = bestTakeOffTime - x.C
            if (G > len(currentGateList)):
                bestGateTime = minGateReachTime
            else:
                listMinGateTime = min(currentGateList)
                bestGateTime = max(listMinGateTime, minGateReachTime)
        if bestGateTime == 0:
            if (L > len(currentLandList)):
                bestLandTime = 0
            else:
                bestLandTime = min(currentLandList)
        else:
            minLandTime = bestGateTime - x.M
            if (L > len(currentLandList)):
                bestLandTime = minLandTime
            else:
                listMinLandTime = min(currentLandList)
                bestLandTime = max(listMinLandTime, minLandTime)

        if bestLandTime < 0:
            bestLandTime = 0

        if (bestLandTime > x.R):
            continue
        else:
            x.L = bestLandTime
            x.G = bestLandTime + x.M
            x.T = max(x.G + x.S, bestTakeOffTime)
            clone_currentTakeOffList = currentTakeOffList[:]
            clone_currentLandList = currentLandList[:]
            clone_currentGateList = currentGateList[:]

            if (T == len(currentTakeOffList)):
                clone_currentTakeOffList.remove(bestTakeOffTime)
            clone_currentTakeOffList.append(x.T + x.O)
            if (G == len(currentGateList)):
                if listMinGateTime in clone_currentGateList:
                    clone_currentGateList.remove(listMinGateTime)
                elif bestGateTime in clone_currentGateList:
                    clone_currentGateList.remove(bestGateTime)
            clone_currentGateList.append(x.T)
            if (L == len(currentLandList)):
                if listMinLandTime in clone_currentLandList:
                    clone_currentLandList.remove(listMinLandTime)
                elif bestLandTime in clone_currentLandList:
                    clone_currentLandList.remove(bestLandTime)
            clone_currentLandList.append(bestLandTime + x.M)

            clone_currentFlightList = currentFlightList[:]
            clone_currentFlightList.remove(x)
            clone_completedFlightList = completedFlightList[:]
            clone_completedFlightList.append(x)
            getFlightOrder(clone_currentFlightList, clone_currentLandList, clone_currentGateList,
                           clone_currentTakeOffList, L, G, T, clone_completedFlightList)

flights = [];
f = open("input.txt")
lines = f.readlines();
L, G, T = lines[0].strip('\n').strip('\r').split();
L = int(L);
G = int(G);
T = int(T);
N = int(lines[1].strip('\n').strip('\r'));

for i in range(2, N + 2):
    R, M, S, O, C = lines[i].strip('\n').strip('\r').split();
    f = Flight(int(R), int(M), int(S), int(O), int(C));
    flights.append(f)
sorted_flights = sorted(flights, key=lambda x: x.R)
getFlightOrder(sorted_flights, [], [], [], L, G, T, [])
