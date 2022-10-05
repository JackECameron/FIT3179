# format data

import re

raw = open("Q4FRV_raw.txt", "r", encoding='utf-8')

headers = ["dis", "sNumber", "sTag", "servArea", "totInc", "emInc", "numStand", "perMet", "90Avg"]

numCols = len(headers)

newFile = open("Q4FRV_step1.csv", "w")

newFile.write(",".join(headers)+"\n")
print(",".join(headers)+"\n")

for line in raw:
    newLine = ""
    #line = line.strip().split("‐")
    line = line.strip().split("-")
    if len(line) != 2:
        print("error")

    first = line[0].strip().split(" ")
    i = 0
    while i < len(first):
        try:
            int(first[i])
            break
        except:
            i += 1
            continue
    station = first[i]
    dis = " ".join(first[0:i])

    newLine += dis.strip() + ","
    newLine += station.strip() + ","
    newLine += "FS" + station.strip()


    
    other = line[1].strip()

    
    match = re.match(r"(^[a-z][a-z ]*)([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+[.][0-9]+[%]) ([0-9]+[.][0-9]+)", other, flags=re.IGNORECASE)

    if match:
        items = match.groups()
        for item in items:
            newLine += ","
            newLine += item.strip() 
    else:
        print("fail")
        print(other)

    newFile.write(newLine+"\n")
newFile.close()
        

