# Aufgabe:
#
# Im Ordner "data/names" gibt es einige Textdateien, die Namen von Personen enthalten (zufällig generiert).
#
# Schreibe ein Programm, welches alle Textdateien aus dem Ordner "names" einliest, und ermittelt, wie oft der Name
# "Max" insgesamt in allen Dateien vorkommt.
#
# Beispiel:
# Käme der Name "Max" in der Datei "1.txt" 1x vor, und in der Datei "2.txt" 2x, sonst aber nie, soll das Programm
# die Zahl 3 ausgeben.

import os

# setting the path for the data set
folder = os.path.join(os.path.dirname(__file__), "./data/names")

# counter for Max
max_count = 0

for file in os.listdir(folder):
    name_file = os.path.join(folder, file)

    # check ever line in every file for 'Max' and increase the counter if we found on
    with open(name_file, "r", encoding="utf-8") as txtfile:
        for line in txtfile:
            person = line.strip().split(" ")
            
            if person[0] == "Max":
                max_count += 1

print(max_count)


