import copy
newFile = open("combinedLong_barchart.csv", "w")


with open("FRV_total_combined_2.csv", "r") as data:
    
    headers = data.readline().strip().split(",")
    headers[4] = "incType"
    headers[5] = "numInc"
    newFile.write(",".join(headers) + "\n")
    
    for line in data:
        
        line = line.strip().split(",")
        inc = line[4]
        emerg = line[5]
        
        nonEmerg = str(int(inc)-int(emerg))

        line2 = copy.deepcopy(line)

        line[4] = "nonInc"
        line2[4] = "emInc"

        line[5] = nonEmerg
        line2[5] = emerg

        newFile.write(",".join(line)+"\n")
        newFile.write(",".join(line2)+"\n")
        

        
newFile.close()
        
