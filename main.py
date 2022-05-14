import csv
word = ''
csv = csv.reader(open(r'C:/Users/migue/Data.csv'))
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


