number = 6
result = 0
result = (number * 2 + 10) / 2
# Schreibe die Berechnung in folgende Zeile
int_result = int(result)

print (int_result)
print("Du hast " + str(number) + " ausgewählt, das magische Ergebnis ist " + str(int_result) + "!")

mail = "willy.wizard@zauberschule.de"
name = mail.split("@")
print(name[0])

mail2 = "info@helena-hexe.com"
name2 = mail2.split("@")
name3 = name2[1].split(".")
print(name3[0])

mail10 = "zarah.zauber@zauberberg.de"
mail20 = "info@trixie-trickser.com"
mail30 = "uwe_unhold@dunkelnetz.de" 

clients = []

clients.append(mail10)
clients.append(mail20)
clients.append(mail30)
# Füge hier mail1, mail2, mail3 zur clients - Liste hinzu

print(clients)
print(len(clients))

zauberer = ["Buehnenzauberer", "magic.com"]
print("@".join(zauberer))
