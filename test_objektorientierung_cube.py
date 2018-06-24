# Aufgabe 1: Modelliere einen Würfel
# Erstelle eine Klasse Cube, mit der du einen Würfel modellierst! Die Würfel-Klasse soll 
# als Eigenschaft die Länge einer Würfel-Seite besitzen. Darüber hinaus soll die Klasse auch 
# zwei Methoden haben: die Methode volume() berechnet das Volumen und gibt es aus, 
# die Methode surface() berechnet die Oberfläche und gibt sie aus.

class Cube():
    def __init__(self, side_len):
        self.side_len = side_len
    
    # calculate volume and print it
    def volume(self):
        print(self.side_len ** 3)
        
    # calculate surface and print it
    def surface(self):
        print(6 * (self.side_len ** 2))
        

# initialze an instance of Cube
a = Cube(3)

a.surface()
a.volume()