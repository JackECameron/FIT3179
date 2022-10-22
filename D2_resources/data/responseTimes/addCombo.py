import copy
newFile = open("combinedLong_barchart_2.csv", "w")


with open("combinedLong_barchart.csv", "r") as data:
    
    headers = data.readline().strip().split(",")
    newFile.write("description" + "," + ",".join(headers) + "\n")


    while True:

        try:
            line1 = data.readline()
            line1 = line1.strip().split(",")
            inc1 = int(line1[5])

            line2 = data.readline()
            line2 = line2.strip().split(",")
            inc2 = int(line2[5])

            tot = inc1 + inc2

            newFile.write("Non-Emergency Incident" + "," + ",".join(line1) + "\n")
            newFile.write("Emergency Incident" + "," + ",".join(line2) + "\n")


            cop = line1.copy()
            cop[4] = "totInc"
            cop[5] = str(tot)
            
            newFile.write("District Total Incidents Average" + "," + ",".join(cop) + "\n")


        except:
            print(line1)
            print(line2)
            break
            
        

newFile.close()
        
