# Format of csv file: Id, Name, Year, Gender, State, Count

dict_names = {}

# open the csv file with all names
with open("data/names.csv", "r") as file:
    for line in file:
        # putting the csv elements in a list, remove linebreaks
        splitted_line = line.strip().split(",")
        
        # jumping over line 1 (header)
        if "Id" in splitted_line:
            continue

        name = splitted_line[1]
        count = int(splitted_line[5])

        # adding names to the dict and summary the count
        if name in dict_names:
            dict_names[name] += count
        else:
            dict_names[name] = count
    
    name_count = 0
    name = " "

    # searching for the most used name
    for key, value in dict_names.items():
        if name_count < value:
            name_count = value
            name = key

    # print the most used name and how often it was given
    print(name)
    print(name_count)