 # Lesson: working with csv files
 # Format of csv file: Id, Name, Year, Gender, State, Count

max_count = 0

# open file
with open("./data/names.csv", "r") as file:

    # find out how many Max were born in CA between 1950 and 2000
    for line in file:
        # putting the csv elements in a list, remove linebreaks
        splitted_line = line.strip().split(",")
        # jumping over line 1 (header)
        if "Id" in splitted_line:
            continue
        # check for target data
        if splitted_line[1] == "Max" and splitted_line[4] == "CA" and int(splitted_line[2]) >= 1950 and\
            int(splitted_line[2]) <= 2000 and splitted_line[3] == "M":
            max_count += int(splitted_line[5])
        else:
            continue
            
# print result        
print(max_count)