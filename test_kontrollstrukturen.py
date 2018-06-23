# Lesson: Loops and conditions

# 1. Aufgabe: Kontinente
# a. Gib nacheinander alle Kontinente aus der Liste continents aus.

continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for continent in continents:
    print(continent)


# b. Gib aus der Liste continents nur die bewohnten Kontinente aus.    

for continent in continents:
    if continent == "Antarktis":
        continue
    print(continent)


# c. Gib aus der Liste stuff nur die Kontinente aus. Du kannst dafür die Liste stuff mit einer Schleife durchgehen 
#    und dann mit Hilfe der Variable continents prüfen, ob ein Element der Liste stuff auch in der Liste continents vorkommt.

stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]

for s in stuff:
    if s in continents:
        print(s)


# d. Wie viele Kontinente sind in der Liste stuff enthalten?

stuff_cont = []

for s in stuff:
    if s in continents:
        print(s)
        stuff_cont.append(s)
print(len(stuff_cont))


# 2. Aufgabe: Rabattaktion
# a. Gib für die Variable price den neuen, rabattierten Preis aus.
# Artikel, die zwischen 0 und 20 (einschließlich) Taler kosten, werden um 20 % reduziert; Artikel, die zwischen 20 (nicht einschließlich) 
# und 50 Taler (einschließlich) kosten,  werden um 40 % reduziert. Alle anderen Artikel, also solche, die mehr als 50 Taler kosten, werden 
# um 60 % reduziert.

price = 50

if price <= 20:
    price *= 0.8
elif price > 20 and price <= 50:
    price *= 0.6
else:
    price *= 0.4      

print(price)


# b. Berechne nun für jeden der alten Preise aus der Liste prices die passenden reduzierten Preise und speichere sie 
# in der neuen Liste new_prices. Gib diese Liste schließlich aus.

prices = [2, 50, 70, 30]
new_prices =[]

for price in prices:
    if price <= 20:
        price *= 0.8
    elif price > 20 and price <= 50:
        price *= 0.6
    else:
        price *= 0.4
    new_prices.append(price)     


# print(new_prices) 
# print()

# c. Zusatzaufgabe (schwierig!)
# Gehe die Elemente in der Liste chaos durch. Bei einem neuen Preis ziehst du bloß den neuen Wert aus dem String und hängst 
# ihn der Liste order an. Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest den neuen Preis und hängst 
# diesen Wert an die Liste order.
#Schließlich gibst du die vollständige Liste order aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!).
# Tipp: Mit Hilfe des in - Operators kannst du prüfen, ob old oder new in einem Listenelement vorkommt ("old" in "old price: 123"), 
# und entsprechend entscheiden, ob du die Rabatierung durchführen möchtest oder nicht.

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for element in chaos:
    if "new" in element:
        order.append(element.split(": ")[1])
    elif "old" in element:
        price = int(element.split(": ")[1])
        if price <= 20:
            price *= 0.8
        elif price > 20 and price <= 50:
            price *= 0.6
        else:
            price *= 0.4
        order.append(price)              
    
print(order)

