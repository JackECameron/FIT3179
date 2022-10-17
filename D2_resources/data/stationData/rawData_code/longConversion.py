
newFile = open("stationData_long.csv", "w")
with open("stationData_complete.csv", "r") as data:
    newFile.write("stationNum,totalPumpers,totalAerial,totalSpec,totP,totA\n")
    data.readline()
    for line in data:
        currentData = []
        line = line.strip().split(",")
        
        for i in [0,1,2,3,5,6]:
            currentData.append(line[i])


        newFile.write(",".join(currentData) + "\n")

        

newFile.close()
