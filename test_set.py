# check how many different firstnames are in names.csv
# Format of csv file: Id, Name, Year, Gender, State, Count

with open("./data/names.csv", "r") as file:

    names = set()
    line_counter = 0

    for line in file:
        # putting the csv elements in a list, remove linebreaks
        splitted_line = line.strip().split(",")      
        # skip header line
        if line_counter != 0:
            names.add(splitted_line[1])
        line_counter += 1
        

# print result        
print(len(names))