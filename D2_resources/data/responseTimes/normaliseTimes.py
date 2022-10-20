newFile = open("FRV_total_combined_3.csv", "w")

with open("FRV_total_combined_2.csv", "r") as data:
    header = data.readline().strip()
    header = header + "normTime" + "\n"
    newFile.write(header)
    for line in data:
        line = line.strip().split(",")
        t = float(line[8])
        nT = round(t/7.7, 2)
        line.append(str(nT))
        line = ",".join(line) + "\n"
        
        newFile.write(line)
newFile.close()
