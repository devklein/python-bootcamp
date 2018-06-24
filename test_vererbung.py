#1. Aufgabe
#Vervollständige die Klasse "FileReader" so, dass bei Aufruf der lines() - Methode die Datei 
#Zeile für Zeile eingelesen wird. Die lines() - Methode soll dann eine Liste der Zeilen in der Datei zurückgeben.

class FileReader():

    def __init__(self, filename):
        self.filename = filename

    def lines(self):
        csv_list = []
        with open(self.filename, "r") as file:
            for line in file:
                csv_list.append(line.strip())
        return csv_list

f = FileReader("./data/datei.csv")
print(f.lines())
print()

# 2. Aufgabe
# Erstelle die Klasse "CsvReader", sodass der "FileReader" erweitert wird. Bei Aufruf der lines() soll die 
# Datei als .csv-Datei eingelesen werden, sprich es soll eine mehrdimensionale Liste zurückgegeben werden.

class CsvReader(FileReader):

    def __init__(self, filename):
        self.filename = filename
        super().__init__(filename)

    def lines(self):
        lines = super().lines()

        # replace with list comprehension
        # splitted_line = []
        # for line in lines:
        #     splitted_line.append(line.split(","))
        # return splitted_line
        
        return [line.split(",") for line in lines]

f = CsvReader("./data/datei.csv")
print(f.lines())