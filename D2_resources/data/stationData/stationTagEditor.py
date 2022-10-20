
newFile = open("stationData_complete_2.csv", "w")

with open("stationData_complete.csv", "r") as data:
    newFile.write("sTag," + data.readline())
    
    for line in data:
        line = line.strip().split(",")
        sTag = line[0]
        if len(line[0]) == 1:
            sTag = "0"+sTag
            
        sTag = "FS" + sTag
         
        newFile.write(sTag + "," + ",".join(line) + "\n")

newFile.close()
