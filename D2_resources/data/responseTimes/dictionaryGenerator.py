
sDict = {}
dict2 = {}
with open("Q1FRV_data.csv", "r") as data:
    data.readline()
    for line in data:
        line = line.strip().split(",")
        if dict2.get(line[0], None) is None:
            dict2[line[0]] = line[0].lower().title()
            
        sDict[line[0]] = sDict.get(line[0], []) + [line[3]]

print(sDict)
print(dict2)

