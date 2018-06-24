# Lesson: functions

# a. Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet!
# Vervollständige die Funktion list_sum, der als Parameter eine Liste mit den Preisen übergeben wird.
# Die Funktion soll dann die Summe der Zahlen aus der Liste ausgeben.

cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):
    total = 0
    for price in l:
        total += price

    print(total)
    
list_sum(cart_prices)


# b. Schreibe eine Funktion, die für einen Artikel eine Preis-Tabelle erstellt!
# Nun wünscht sich die Mathemagierin eine Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann. 
# Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten des Artikels stehen. 
# Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".

def price_table(name, price):
    price_list = []

    for i in range(1, 11):
        price_list.append(str(i) + " x " + name + ": " + str(price * i))
        
    return price_list

print(price_table("Wunderkeks", 0.79))


# c. Schreibe eine Funktion, die die Listen mit den Artikeln auffüllt!
# Von nun an soll auch eine Funktion die Waren in die virtuellen Regale einräumen, d. h. an die erste, noch leere Position 
# in der Liste shelf packen. Als Parameter soll der Funktion add_shelf() der einzusortierende Artikel übergeben werden. 
# Die Funktion aktualisiert dann die Liste shelf, und der neue Artikel wurde in das erste leere Regalfach eingeräumt.

shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_shelf(article):
    for i in range(0, len(shelf)):
        if shelf[i] == "leer":
            shelf[i] = article
            break
   
add_shelf("Rubik's Cube")
print(shelf)