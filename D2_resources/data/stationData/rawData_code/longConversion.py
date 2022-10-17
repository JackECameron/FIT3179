
newFile = open("stationData_long.csv", "w")
with open("stationData_complete.csv", "r") as data:
    newFile.write("stationNum,class,type,quant\n")
    data.readline()
    for line in data:

        line = line.strip().split(",")
        sNum = line[0]
        pump = line[1]
        aerial = line[2]
        spec = line[3]
        pod = line[5]
        appl = line[6]
 
        newFile.write(sNum + "," + "equipment" + "," +"pumper" + "," +pump+"\n")
        newFile.write(sNum + "," + "equipment"+ "," +"aerial"+ "," +aerial+ "\n")
        newFile.write(sNum + "," + "equipment"+"," + "spec"+"," + spec+ "\n")

        newFile.write(sNum + "," + "unit"+ "," +"pod"+"," + pod+ "\n")
        newFile.write(sNum + "," + "unit"+"," + "appl"+"," + appl+ "\n")

        

newFile.close()
