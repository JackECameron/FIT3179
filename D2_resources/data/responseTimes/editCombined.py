
# Get top
top = []
topAgr = []
with open("FRV_total_combined.csv") as data:
    data.readline()
    for line in data:
        line = line.strip().split(",")
        if line[9] == "4" and line[2] != "agr":
            top.append(line[3])
        elif line[9] == "4" and line[2] == "agr":
            topAgr.append(line[3])

newfile = open("FRV_total_combined_2.csv", "w")

with open("FRV_total_combined.csv") as data:
    newfile.write(data.readline().strip() +",rankQ4" + "\n")
    
    for line in data:
        line = line.strip().split(",")
        if line[9] != "4":
            if line[2] != "agr":
                ind = top.index(line[3])+1
                newfile.write(",".join(line) + "," + str(ind) + "\n")
            else:
                ind = topAgr.index(line[3])+1
                newfile.write(",".join(line) + "," + str(ind) + "\n")
        else:
            ind = line[-1]
            newfile.write(",".join(line) + "," + str(ind)+ "\n")
            
newfile.close()
