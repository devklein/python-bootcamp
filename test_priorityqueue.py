# Ermittle den 5.-häufigsten Vornamen, der in den USA vergeben wurde! 
# Lies dazu die ../data/names.csv - Datei ein. Verwende dazu zuerst ein Dictionary, mit dem du # die Häufigkeit 
# der Vornamen zählst und anschließend eine PriorityQueue, um die Top 5 Vornamen zu ermitteln.

# Format of csv file: Id, Name, Year, Gender, State, Count
import queue
import csv

with open('./data/names.csv', newline='') as csvfile:
    namefile = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    name_dict = {}
    line_counter = 0

    for line in namefile:
        # skip header line        
        if line_counter != 0:
            # assign names and names count to variables
            name = line[1]
            name_count = int(line[5])

            # check if name is already in dict sum up the name count
            if name in name_dict:
                name_dict[name] += name_count
            else:
                name_dict[name] = name_count
        
        line_counter += 1

    # write names and name count in a priority queue
    name_queue = queue.PriorityQueue()
    for name, number in name_dict.items():
        name_queue.put((-number, name))

# print the five most given name
for i in range(5):
    print(name_queue.get())
