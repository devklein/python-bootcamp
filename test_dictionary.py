# Id, Name, Year, Gender, State, Count

dict_names = {}


with open("data/names.csv", "r") as file:
    for line in file:
        # putting the csv elements in a list, remove linebreaks
        splittedLine = line.strip().split(",")
        
                # jumping over line 1 (header)
        if "Id" in splittedLine:
            continue

        name = splittedLine[1]
        count = int(splittedLine[5])

        if name in dict_names:
            dict_names[name] += count
        else:
            dict_names[name] = count
    
    name_count = 0
    name = " "

    for key, value in dict_names.items():
        if name_count < value:
            name_count = value
            name = key

    print(name)
    print(name_count)