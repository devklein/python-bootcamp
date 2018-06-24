# Aufgabe 2: Modelliere ein Kugel
# Die Kugel-Klasse soll als Eigenschaft den Radius übergeben bekommen. Zudem soll 
# sie - ähnlich wie der Würfel - zwei Methoden haben: 
# surface() um den Oberflächeninhalt zu berechnen, volume() um das Volumen zu berechnen.
# Damit du diese Berechnungen durchführen kannst, benötigst du die Kreiszahl Pi. Diese steht dir 
# nach einem import math unter math.pi zur Verfügung (was der import - Befehl genau macht, 
# schauen wir uns noch später im Kurs an).

import math

class Ball():
    def __init__(self, radius):
        self.radius = radius
    
    # calculate volume and print it
    def volume(self):
        print(4 / 3 * math.pi * math.pow(self.radius, 3))
 
    # calculate surface and print it
    def surface(self):
        print(4 * math.pi * math.pow(self.radius, 2))


b = Ball(4)
b.surface()
b.volume()