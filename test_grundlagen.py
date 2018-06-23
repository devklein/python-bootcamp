# Lesson: Python basics
# Write some basic Python

# a.

number = 6
result = 0
result = (number * 2 + 10) / 2

int_result = int(result)

print (int_result)
print("Du hast " + str(number) + " ausgewählt, das magische Ergebnis ist " + str(int_result) + "!")

# b.

mail = "willy.wizard@zauberschule.de"
name = mail.split("@")
print(name[0])

mail2 = "info@helena-hexe.com"
name2 = mail2.split("@")
name3 = name2[1].split(".")
print(name3[0])

# c. 

mail10 = "zarah.zauber@zauberberg.de"
mail20 = "info@trixie-trickser.com"
mail30 = "uwe_unhold@dunkelnetz.de" 

clients = []

clients.append(mail10)
clients.append(mail20)
clients.append(mail30)

print(clients)
print(len(clients))

# d. 
zauberer = ["Buehnenzauberer", "magic.com"]
print("@".join(zauberer))
