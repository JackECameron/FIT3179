# Remove percent sign?
data = open("Q4FRV_step1.csv", "r")

headers = data.readline()

newFile = open("Q4FRV_data.csv", "w")

newFile.write(headers)

for line in data:
    line = line.strip().split(",")
    line[7] = line[7].replace("%", "")

    newFile.write(",".join(line)+"\n")
    
newFile.close()
    
