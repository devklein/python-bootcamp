# Aufgabe 3: Modelliere ein Konto
# a. Erstelle die Konto-Klasse Account mit der Eigenschaft Kontostand credits! 
# Diese Eigenschaft wird mit einem Startkapital initialisiert. 
# Die Methode display() soll den aktuellen Kontostand ausgeben.

class Account():
    def __init__(self, credits):
        self.credits = credits

    def display(self):
        print(self.credits)



Kunde111 = Account(500)
Kunde111.display()

# b. Ergänze die Klasse Account um zwei Methoden (pay_in() zum Einzahlen, withdraw() zum Abheben), 
# so dass du Geldbeträge einzahlen und abbuchen kannst, und der Kontostand entsprechend angepasst wird.
# Du sollst nur Geld abheben können, so lange auch Geld auf dem Konto ist. Ein Dispo-Kredit wird nicht gewährt. 
# In dem Fall soll eine Fehlermeldung ausgegeben werden, in der steht, wieviel Geld maximal abgebucht werden kann.

class Account():
    
    def __init__(self, credits):
        self.credits = credits

    def display(self):
        print(self.credits)

    def pay_in(self, cash_in):
        self.credits += cash_in

    def withdraw(self, cash_out):
        if cash_out > self.credits:
            print("Du kannst nur noch " +  str(self.credits) + " Euro abheben!")
        else:
            self.credits -= cash_out

Kunde111 = Account(500)
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25)
Kunde111.display()
Kunde111.withdraw(600)


# c. Bislang ist das Konto noch ungeschützt - wir brauchen eine PIN! Ergänze in der Klasse die Eigenschaft pin! 
# So wie mit dem Startkapital soll das Konto auch mit einer PIN initialisiert werden. Von nun an muss man beim Geldabheben 
# nicht nur den Betrag, sondern auch die PIN angeben: Nur wenn die PIN mit der des Kontos übereinstimmt, kann auch Geld 
# abgebucht werden, ansonsten kommt es zu einer Fehlermeldung!

class Account():
    
    def __init__(self, credits, pin):
        self.credits = credits
        self.pin = pin

    def display(self):
        print(self.credits)

    def pay_in(self, cash_in):
        self.credits += cash_in

    def withdraw(self, cash_out, pin):
        if pin == self.pin:
            if cash_out > self.credits:
                print("Du kannst nur noch " +  str(self.credits) + " abheben")
            else:
                self.credits -= cash_out
        else:
            print("Falsche PIN! Konto gesperrt! Du bist verhaftet! Hände hoch!")


Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25, "1234")
Kunde111.display()
Kunde111.withdraw(600, "12345")