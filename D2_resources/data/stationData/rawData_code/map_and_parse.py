# create mapping dictionary
import re
mapData = open("mappings.txt", "r")

header = mapData.readline().strip().split(",")

mappings  = {}

for mapping in mapData:
    current = mapping.strip().split(",")

    mappings[current[0].strip()] = [current[1].strip(), current[2].strip()]
    
# Function to generate data

def computeStationData(pString, aString, sString):
    # resolve pumper
    pString = pString.replace('"', '')
    pumper = pString.strip().split(",")
    pumper = [i for i in pumper if i != "x"]
    pumper = [re.findall("^[A-Z]*", i.strip())[0] for i in pumper]

    # resolve aerial
    aString = aString.replace('"', '')
    aerial = aString.strip().split(",")
    aerial = [i for i in aerial if i != "x"]
    aerial = [re.findall("^[A-Z]*", i.strip())[0] for i in aerial]
    

    # resolve special and support
    sString = sString.replace('"', '')
    specSup = sString.strip().split(",")
    specSup = [i for i in specSup if i != "x"]
    specSup = [re.findall("^[A-Z]*", i.strip())[0] for i in specSup]

    # Compute stats
    stationData1 = {equip: 0 for equip in mappings.keys()}

    # combined
    combined = pumper+aerial+specSup

    
    stationData2 = {"totalPumpers": len(pumper), "totalAerial": len(aerial), "totalSpec": len(specSup), "grandTotal": len(combined), "totP": 0, "totA": 0}
    for thing in combined:
        try:
            data = mappings[thing]
            stationData2["tot"+data[1]] = stationData2["tot"+data[1]] + 1
        
        except:
            print("Failed Lookup 1")
            print(thing)

        try:
            data = mappings[thing]
            stationData1[thing] = stationData1[thing] + 1
        
        except:
            print("Failed Lookup 2")

    return {"dataSet1": stationData1, "dataSet2": stationData2}
            
    
# Create new CSV table for stations using mappins (column for each key)

rawStation = open("stationEquipment.txt", "r")
header2 = rawStation.readline()

stationData = {}

for station in rawStation:
    current = station.strip().split("\t")


    stationNumber = current[0]
    pumperString = current[1]
    aerialString = current[2]
    specSupString = current[3]

    stationData[stationNumber] = computeStationData(pumperString, aerialString, specSupString)


# write station data to file

newFile = open("stationData_complete.csv", "w")

newHeader = "stationNum,"+",".join(["totalPumpers", "totalAerial", "totalSpec", "grandTotal", "totP", "totA"] + list(mappings.keys())) + "\n"

newFile.write(newHeader)

for station in stationData.keys():
    currentData = stationData[station]
    line = station
    # add stats
    for stat in currentData["dataSet2"].keys():
        line = line + "," + str(currentData["dataSet2"][stat])

    # add Equipment
    for equip in currentData["dataSet1"].keys():
        line = line + "," + str(currentData["dataSet1"][equip])

    line = line + "\n"

    newFile.write(line)

    
    
newFile.close()
    
