# Aufgabe 1
# Vervollständige die Funktion shortest_word(): Ihr sollen mehrere Strings übergeben 
# werden (KEINE Liste von Strings!), von denen sie den String mit den wenigsten Zeichen zurückliefert.

def shortest_word(*nameslist):
    short_name = nameslist[0]
    for name in nameslist:
        if len(name) < len(short_name):
            short_name = name
    return short_name    
   
print(shortest_word("Max", "Moritz", "Monika", "Tim", "Jo"))


# Aufgabe 2
# a. Sortiere die Tupel in der Liste tupels aufsteigend nach ihrer Summe!
# Hinweis: Schreibe dazu zuerst eine normale Funktion und löse die Aufgabe 
# anschließend nochmal mit einer lambda-Funktion.

# normale Funktion

tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]

def tupels_key(sum):
    return sum[0] + sum [1]

tupels.sort(key=tupels_key)
print(tupels)

# lambda Funktion

tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]

tupels.sort(key = lambda n: n[0] + n[1])
print(tupels)

# b. Sortiere die Liste names mit Namen nach dem Nachnamen. Du kannst annehmen, dass alle Namen 
# in der Liste nur einen Vornamen enthalten. Das Format der Namen ist immer "Vorname Nachname".
# Überlege dir dazu zuerst, wie du den Nachnamen ermittelst und schreibe dann die entsprechende 
# Funktion, die du der .sort()- Funktion übergibst.

# normale Funktion

names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

def names_key(abc):
    return abc.split()[1]

names.sort(key = names_key)

print(names)

# lambda Funktion

names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

names.sort(key = lambda n: n.split()[1])

print(names)

#c. Sortiere die Liste sentences absteigend nach der Anzahl der Wörter, die ein Element aus 
# sentences jeweils enthält. Du kannst annehmen, dass in den Sätzen alle Wörter ordnungsgemäß 
# mit Leerzeichen voneinander getrennt sind. :-) Überlege dir dazu zuerst, wie du die Anzahl 
# Wörter in einem Satz ermitteln kannst.

# normal function

sentences = ["Sie liefen weiter den Strand entlang.", "Der Hund bellte laut.", "Er rutschte aus.", "Sie lachte."]

def s_key(sent):
        # morge complex way
        # counter = 0
        # for s in sentences:
        #     sentences.find(" ")
        #     counter += 1
        # return counter
        #smart way
        return len(sent.split())


sentences.sort(key = s_key)
print(sentences)

# lambda function

sentences = ["Sie liefen weiter den Strand entlang.", "Der Hund bellte laut.", "Er rutschte aus.", "Sie lachte."]

sentences.sort(key = lambda sent: len(sent.split()))
print(sentences)

# Zusatzaufgabe
# Verändere den folgenden Code so, dass die Liste l nicht mehr innerhalb der Funktion make_row() 
# überschrieben wird. Die Liste, die make_row() ausgibt, soll also identisch mit der bisherigen 
# sein. l soll aber am Ende in seiner ursprünglichen Form ausgegeben werden.

l = ["o", "x", "o"]

def make_row(row):
    row_new = row.copy()
    row_new[2] = "x"
    print(row_new)
    
make_row(l)
print(l)