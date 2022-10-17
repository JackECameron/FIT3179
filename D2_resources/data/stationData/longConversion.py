
newFile = open("stationData_long.csv", "w")
with open("stationData_complete.csv", "r") as data:
    newFile.write("stationNum,class,type,quant,decrip\n")
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

 
 
        newFile.write(sNum + "," + "equipment" + "," +"pumper" + "," +pump+ "," + "Pumper" + "\n")
        newFile.write(sNum + "," + "equipment"+ "," +"aerial"+ "," +aerial+ "," + "Aerial Support" + "\n")
        newFile.write(sNum + "," + "equipment"+"," + "spec"+"," + spec+ "," + "Special Equipment" + "\n")

        newFile.write(sNum + "," + "unit"+ "," +"pod"+"," + pod + "," +"Pods" + "\n")
        newFile.write(sNum + "," + "unit"+"," + "appl"+"," + appl+ "," +"Appliances" + "\n")

        

newFile.close()
