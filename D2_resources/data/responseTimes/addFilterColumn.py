
newfile = open("FRV_total_combined_filter.csv", "w")

with open("FRV_total_combined.csv") as data:
    newfile.write("filter," + data.readline())
    for line in data:
        line = line.strip().split(",")

        if line[2] == "agr":
            addition = "All Districts,"
        else:
            addition = line[0].title()+","
        newfile.write(addition + ",".join(line) + "\n")
            
newfile.close()
