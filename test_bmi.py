# Aufgabe: Schreibe ein Programmwelches Körpergröße und Gewicht einer Person abfragt und aiuf Basis
# dieser Eingaben den BMI ausrechent und ausgibt.
# Formel für BMI: Gewicht in Kg / Körpergröße in m^2

# version 1
print("Berechne deinen BMI:")
weight = input("Bitte gebe den Körpergewicht in kg ein: ")
size = input("Bitte gebe deine Körpergröße in m ein: ")

bmi = float(weight.replace(",", ".")) / (float(size.replace(",", ".")) ** 2)

print("Dein BMI ist {bmi:.1f}.".format(bmi = bmi))

# version 2
print("Berechne deinen BMI:")
weight = float(input("Bitte gebe den Körpergewicht in kg ein: ").replace(",", "."))
size = float(input("Bitte gebe deine Körpergröße in m ein: ").replace(",", "."))

bmi = weight / size ** 2

print("Dein BMI ist {bmi:.1f}.".format(bmi = bmi))