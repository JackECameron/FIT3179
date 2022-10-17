
newFile = open("stationData_long.csv", "w")
with open("stationData_complete.csv", "r") as data:
    newFile.write("stationNum,class,type,quant,perc,decrip\n")
    data.readline()
    for line in data:

        line = line.strip().split(",")
        total = int(line[4])
        sNum = line[0]
        pump = str(round(100*int(line[1])/total, 2))
        aerial = str(round(100*int(line[2])/total, 2))
        spec = str(round(100*int(line[3])/total, 2))
        pod = str(round(100*int(line[5])/total, 2))
        appl = str(round(100*int(line[6])/total, 2))

        tpump = line[1]
        taerial = line[2]
        tspec = line[3]
        tpod = line[5]
        tappl = line[6]

 
 
        newFile.write(sNum + "," + "equipment" + "," +"pumper" + "," +tpump+ "," +pump+"," + "Pumper Truck" + "\n")
        newFile.write(sNum + "," + "equipment"+ "," +"aerial"+ "," +taerial+ "," +aerial+"," + "Aerial Support" + "\n")
        newFile.write(sNum + "," + "equipment"+"," + "spec"+"," + tspec+ "," +spec+"," + "Specialist Equipment" + "\n")

        newFile.write(sNum + "," + "unit"+ "," +"pod"+"," + tpod + "," +pod+"," +"Pod" + "\n")
        newFile.write(sNum + "," + "unit"+"," + "appl"+"," + tappl+ "," +appl+"," +"Appliance" + "\n")

        

newFile.close()
