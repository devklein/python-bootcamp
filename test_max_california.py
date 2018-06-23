# Id, Name, Year, Gender, State, Count

maxCount = 0

with open("data/names.csv", "r") as file:
    for line in file:
        # putting the csv elements in a list, remove linebreaks
        splittedLine = line.strip().split(",")
        # jumping over line 1 (header)
        if "Id" in splittedLine:
            continue
        # check for target data
        if splittedLine[1] == "Max" and splittedLine[4] == "CA" and int(splittedLine[2]) >= 1950 and\
            int(splittedLine[2]) <= 2000 and splittedLine[3] == "M":
            maxCount += int(splittedLine[5])
        else:
            continue
# print result        
print(maxCount)
    
        
    
    