# Aufgabe 4: Modelliere einen Zug
# a. Jetzt wirst du Zugobjekte bauen! Erstelle die Klasse Train, die mit den Eigenschaften 
# route und position initialisiert wird! Bei route handelt es sich um eine Liste mit den 
# Haltebahnhöfen des Zuges. position steht für den Index des Bahnhofs aus der Liste, an dem 
# sich der Zug gerade befindet bzw. von dem er zuletzt abgefahren ist (wo genau sich der Zug 
# auf der Strecke zwischen zwei Bahnhöfen befindet, interessiert uns hier nicht). Mit der 
# Methode show_station() soll der Name dieses Bahnhofs ausgegeben werden.

class Train():
    def __init__(self, route, position):
        self.route = route
        self.position = position

    def show_station(self):
        print(self.route[self.position])

orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()


# b. Bisher sitzt ein Zug der Klasse Train noch in seinem Startbahnhof fest. Ergänze nun 
# zwei Methoden move() und move_back(), mit denen man einen Zug auf seiner Route zur nächsten 
# bzw. zur vorherigen Station bewegen kann, sofern es diese Station auf der Route gibt. 
# Der Zug darf seine Route nicht verlassen!


class Train():
    def __init__(self, route, position):
        self.route = route
        self.position = position

    def show_station(self):
        print(self.route[self.position])

    def move(self):
        if self.position < len(self.route) - 1:
            self.position += 1
        else:
            print("Endstation! Alle aussteigen!")

    def move_back(self):
        if self.position > 0:
            self.position -= 1
        else:
            print("Anfangsstation! Alle aussteigen!")


orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move_back()
orientexpress.show_station()


# c. Die Route soll nachträglich bearbeitet werden können, indem man mit einer Methode bypass_station() einen 
# anzugebenden Haltebahnhof von der Route entfernt. Der Zug soll dann sicherheitshalber an den Start der Route 
# versetzt werden, sofern er sich nicht schon dort befindet.
# Tipp: Erinnere dich an die Methoden für Listen! :-)

class Train():
    def __init__(self, route, position):
        self.route = route
        self.position = position

    def show_station(self):
        print(self.route[self.position])

    def move(self):
        if self.position < len(self.route) - 1:
            self.position += 1
        else:
            print("Endstation! Alle aussteigen!")

    def move_back(self):
        if self.position > 0:
            self.position -= 1
        else:
            print("Anfangsstation! Alle aussteigen!")

    def bypass_station(self, station):
        self.route.remove(station)
        self.position = 0


orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()


