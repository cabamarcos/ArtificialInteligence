import csv
word = ''
csv = csv.reader(open(r'C:/Users/Marcos Caballero/Downloads/Data.csv'))
ListOfWords = []
list = []
for i in csv:
    for str in i:
        for letter in str:
            if letter == 'N' or letter == 'E' or letter == 'W':
                list.append(word)
                word = letter
                list.append(word)
                word = ''
            elif letter == ';':
                pass
            else:
                word += letter
        list.append(word)
        ListOfWords.append(list)
        word = ''
        list = []

lights=["N", "E", "W"]
DictionaryOfProbabilities = {"N":0, "E":0, "W":0}
HL=["HighHighHigh", "HighHighLow", "HighLowHigh", "HighLowLow",
                      "LowHighHigh", "LowHighLow", "LowLowHigh", "LowLowLow"]

def funcDictionaryOfProbabilities():
    a=0
    while a != 3:
        list_probabilities=[]
        b=0
        while b != 8:
            Probabilities = []
            sum=0
            c=0
            while c != 8:
                count=0
                for words in ListOfWords:
                    if words[1] == lights[a] and words[0] == HL[b] and words[2] == HL[c]:
                        count+=1
                Probabilities.append(count)
                c+=1
            j=0
            for j in range(8):
                sum = sum + Probabilities[j]
            j=0
            while j != 8 and sum!=0:
                Probabilities[j]=Probabilities[j]/sum
                j+=1
            list_probabilities.append(Probabilities)
            b+=1
        if a == 0:
            DictionaryOfProbabilities["N"] = list_probabilities
        if a == 1:
            DictionaryOfProbabilities["E"] = list_probabilities
        else:
            DictionaryOfProbabilities["W"] = list_probabilities
        a+=1
funcDictionaryOfProbabilities()
print(DictionaryOfProbabilities)
V1 = {"HighHighHigh": [0], "HighHighLow": [0], "HighLowHigh": [0], "HighLowLow": [0], "LowHighHigh": [0], "LowHighLow": [0], "LowLowHigh": [0], "LowLowLow": [0]}
V2 = {"HighHighHigh": [0, 0], "HighHighLow": [0, 0], "HighLowHigh": [0, 0], "HighLowLow": [0, 0],"LowHighHigh": [0, 0], "LowHighLow": [0, 0], "LowLowHigh": [0, 0], "LowLowLow": [0, 0]}
iterations = 0
continuee = True
while continuee:
    iterations+= 1
    for FirstRoadLights in HL[0:]:
        costs = {"N": 1, "E": 1, "W": 1}
        for action in lights:
            BellmanProbability = 0
            for SecondRoadLights in HL:
                BellmanProbability += DictionaryOfProbabilities[action][HL.index(FirstRoadLights)][HL.index(SecondRoadLights)] * V1[SecondRoadLights][0]
            costs[action] += BellmanProbability
        MinimumCostOfActions=min(costs["N"], costs["E"], costs["W"])
        V2[FirstRoadLights][0] =MinimumCostOfActions
        if costs["N"] == V2[FirstRoadLights][0]:
            V2[FirstRoadLights][1] = "N"
        if costs["E"] == V2[FirstRoadLights][0]:
            V2[FirstRoadLights][1] = "E"
        if costs["W"] == V2[FirstRoadLights][0]:
            V2[FirstRoadLights][1] = "W"
    continuee = False
    for FirstRoadLights in HL:
        if (V2[FirstRoadLights][0] - V1[FirstRoadLights][0]) > 0.001:
            continuee = True
        V1[FirstRoadLights][0] = V2[FirstRoadLights][0]
print(V2)
print(iterations,"is the number of iterations.")