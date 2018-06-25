# check how many different firstnames are in names.csv
# Format of csv file: Id, Name, Year, Gender, State, Count

import csv

with open("./data/names.csv", "r") as file:

    names = set()

    for line in file:
        # putting the csv elements in a list, remove linebreaks
        splitted_line = line.strip().split(",")      
        if "Id" not in splitted_line:
            names.add(splitted_line[1])
        else:
            # jumping over line 1 (header)
            continue

# print result        
print(len(names))