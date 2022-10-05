from operator import add
import math
data = open("Q4FRV_data.csv", "r")

data.readline()
newHeaders = ",".join(["dis", "sNumber", "totInc_a", "emInc_a", "numStand_a", "perMet_a", "90Avg_a"])

newFile = open("Q4FRV_agr.csv", "w")

newFile.write(newHeaders+"\n")


districts = {}

for line in data:
    line = line.strip().split(",")
    d = line[0]
    numInc = int(line[4])
    numEm = int(line[5])
    numStandards = int(line[6])
    perc = float(line[7])
    avg90 = float(line[8])

    districts[d] = list( map(add, districts.get(d, [0, 0, 0, 0, 0, 0]), [1, numInc, numEm, numStandards, perc, avg90]))
    
for dis in districts.keys():
    districts[dis][1] /= districts[dis][0]
    districts[dis][2] /= districts[dis][0]
    districts[dis][3] /= districts[dis][0]
    districts[dis][4] /= districts[dis][0]
    districts[dis][5] /= districts[dis][0]

    districts[dis][1] = math.ceil(districts[dis][1])
    districts[dis][2] = math.ceil(districts[dis][2])
    districts[dis][3] = math.ceil(districts[dis][3])
    districts[dis][4] = round(districts[dis][4], 2)
    districts[dis][5] = round(districts[dis][5], 2)
        


    newFile.write(dis + "," +  ",".join([str(districts[dis][i]) for i in range(len(districts[dis]))])+"\n")
    
newFile.close()
    
