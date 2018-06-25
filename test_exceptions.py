# a. Schreibe eine Exception, die den Fehler abfängt, wenn jemand versucht die folgende 
# Datei zu öffnen, die nicht in diesem Verzeichnis existiert! Gib in dem Fall die 
# Nachricht "Datei wurde nicht gefunden" aus. Achte auch darauf, die Datei mit einem geeigneten 
# Konstrukt zu öffnen, falls sie zukünftig doch existieren sollte - ohne, dass es dann zu Fehlern 
# kommen kann, weil die Datei nicht richtig geschlossen wurde.

try:
    with open("nicht_oeffnen.txt", "r") as file:
        print(file)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")

# b. Schau dir an, welcher Fehlertyp bei der Ausführung des folgenden Code auftritt. Fange den Fehler 
# mit try except ab und gib eine passende Fehlermeldung aus!    

articles = ["Unsichtbare Tastatur", "Holographisches Display", "Endlosschleifenschneider"]

prices = {"Unsichtbare Tastatur": 150, "Holographisches Display": 1150}

def print_prices():
    for article in articles:
        print(prices[article])

try:
    print_prices()
except KeyError:
    print("Artikel nicht in Preisliste vorhanden")

# c. Zuletzt erstellst du noch eine Fehlerklasse, die aufgerufen wird, wenn es sich bei d um ein 
# leeres dictionary handelt. Dann soll ein EmptyDictionaryError auftreten mit dem Hinweis, dass 
# das dictionary d kein Element enthält.    

d = {}

class EmptyDictionaryError(Exception):
    pass

if len(d) == 0:
    raise EmptyDictionaryError("Das Dictionary is leer")
    