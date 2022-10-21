
newfile = open("FRV_total_combined_dif.csv", "w")

with open("FRV_total_combined_2.csv") as data:
    newfile.write(data.readline().strip() + "," + "dif\n")
    
    for line in data:
        line = line.strip().split(",")
        dif = str(float(line[8])-7.7)
        newfile.write(",".join(line) + ","+dif+ "\n")
            
newfile.close()
