import copy
class Solution:
    def __init__(self):
        self.matrix = []
        f = open("input.txt");
        lines = f.readlines();
        n = int(lines[0].strip("\n"));

        for i in range(1, n+1):
            y = lines[i].strip('\n').strip('\r');
            lis = [x for x in y];
            self.matrix.append(lis);
        dictionary = {}
        dictionary_new = {}
        blockedList=[]
        self.DP = {}

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]=='1' or self.matrix[i][j]=='2':
                    a, b = self.getScoreBlock(i,j,self.matrix)
                    blockedList.extend(b)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]=='0' and not str(i)+"_"+str(j) in blockedList:
                    temp_list = []
                    temp_score, temp_blocks= self.getScoreBlock(i,j,self.matrix)
                    temp_list.append(temp_score)
                    temp_list.append(temp_blocks)           
                    dictionary[str(i)+"_"+str(j)]= temp_list

        if n>6:
            z = []
            dictionary_highest={}
            o = open("output.txt", "w")
            for w in dictionary:
                sum = 0
                for k in dictionary[w][1]:
                    if k in dictionary:
                        sum += dictionary[k][0]
                        x = dictionary[w][0] + sum
                dictionary_highest[w] = x
            z = sorted(dictionary_highest, key=dictionary_highest.get, reverse=True)

            string = z[0].split("_")
            o.write(string[0] + " " + string[1])
            o.close()

        if n<=6:
            dictionary_new = dictionary
            o=open("output.txt","w")
            if len(dictionary) != 0:
                string = self.minimax(dictionary_new, 0, 0, [], []).split("_")
                o.write(string[0]+" "+string[1])
            o.close()
    def getKey(self, pickedListA, pickedListB, x):
        pickedListA.sort()
        pickedListB.sort()
        return str(pickedListA) + str(pickedListB)+ x
    
    def removedictionary(self,temp_dictionary,x):
        blockedList=temp_dictionary[x][1]
        temp_dictionary.pop(x)
        for temp in blockedList:
            if temp in temp_dictionary:
                temp_dictionary.pop(temp)

    def minimax(self, dictionary, currentScoreA, currentScoreB, pickedPositionsA, pickedPositionsB):
        currentScoreA=0
        currentScoreB=0
        currentBestPick= None;
        currentMax=-1
        currentB = -1
        pickedPositionsA=[]
        pickedPositionsB=[]
        for i in dictionary:
            temp_dictionary=copy.deepcopy(dictionary)
            temp_pickedPositionsA=copy.deepcopy(pickedPositionsA)
            currentScoreA = dictionary[i][0]
            self.removedictionary(temp_dictionary,i)
            temp_pickedPositionsA.append(i)
            if len(temp_dictionary)!=0:
                a,b=self.pickBestB(temp_dictionary, currentScoreA, currentScoreB, temp_pickedPositionsA,pickedPositionsB)
                if a> currentMax:
                    currentMax = a
                    currentB = b
                    currentBestPick = i
        return currentBestPick
    def pickBestA(self, dictionary, currentScoreA, currentScoreB, pickedPositionsA, pickedPositionsB):
        key = self.getKey(pickedPositionsA, pickedPositionsB, 'A')
        if key in self.DP:
            return self.DP[key]

        currentMax=currentScoreA
        currentB = currentScoreB
        for i in dictionary:
            temp_dictionary=copy.deepcopy(dictionary)
            temp_pickedPositionsA=copy.deepcopy(pickedPositionsA)
            currentScoreA+=dictionary[i][0]
            self.removedictionary(temp_dictionary,i)
            temp_pickedPositionsA.append(i)
            if len(temp_dictionary)!=0:
                a,b=self.pickBestB(temp_dictionary, currentScoreA, currentScoreB, temp_pickedPositionsA,pickedPositionsB)
                if a> currentMax:
                    currentMax = a
                    currentB = b
                currentScoreA -= dictionary[i][0]


        self.DP[key] = [currentMax, currentB]
        return self.DP[key]
    
        
    def pickBestB(self, dictionary, currentScoreA, currentScoreB, pickedPositionsA, pickedPositionsB):
        key = self.getKey(pickedPositionsA, pickedPositionsB, 'B')
        if key in self.DP:
            return self.DP[key]
        currentMax = -1
        currentA = currentScoreA
        for i in dictionary:
            temp_dictionary=copy.deepcopy(dictionary)
            temp_pickedPositionsB=copy.deepcopy(pickedPositionsB)
            currentScoreB+=dictionary[i][0]
            self.removedictionary(temp_dictionary,i)
            temp_pickedPositionsB.append(i)
            if len(temp_dictionary)!=0:
                a,b=self.pickBestA(temp_dictionary, currentScoreA, currentScoreB, pickedPositionsA,temp_pickedPositionsB)
                if b> currentMax:
                    currentMax = b
                    currentA = a
                currentScoreB -= dictionary[i][0]
        self.DP[key] = [currentA, currentMax]
        return self.DP[key]
        


    def getScoreBlock(self,i,j,matrix):
        score=1
        coveredBlocks=[]
        for k in range(1,4):
            if i-k>=0 and j-k>=0 and matrix[i-k][j-k]=='0':
                score+=1
                coveredBlocks.append(str(i-k)+"_"+str(j-k))
            else:
                break;
        for k in range(1,4):
            if i+k<len(self.matrix) and j+k<len(self.matrix) and matrix[i+k][j+k]=='0':
                score+=1
                coveredBlocks.append(str(i+k) + "_" + str(j+k))
            else:
                break;
        for k in range(1,4):
            if i-k>=0 and j+k<len(self.matrix) and matrix[i-k][j+k]=='0':
                score+=1
                coveredBlocks.append(str(i-k) + "_" + str(j+k))
            else:
                break;
        for k in range(1,4):
            if i+k<len(self.matrix) and j-k>=0 and matrix[i+k][j-k]=='0':
                score+=1
                coveredBlocks.append(str(i+k) + "_" + str(j-k))
            else:
                break;
        for k in range(1,4):
            if j-k>=0 and matrix[i][j-k]=='0':
                score+=1
                coveredBlocks.append(str(i) + "_" + str(j-k))
            else:
                break;
        for k in range(1,4):
            if j+k<len(self.matrix) and matrix[i][j+k]=='0':
                score+=1
                coveredBlocks.append(str(i) + "_" + str(j+k))
            else:
                break;
        for k in range(1,4):
            if i-k>=0 and matrix[i-k][j]=='0':
                score+=1
                coveredBlocks.append(str(i-k) + "_" + str(j))
            else:
                break;
        for k in range(1,4):
            if i+k<len(self.matrix) and matrix[i+k][j]=='0':
                score+=1
                coveredBlocks.append(str(i+k) + "_" + str(j))
            else:
                break;
        return score, coveredBlocks




sol=Solution();