napis = "ala ma kota"
napis = napis.upper()
napis
napis = napis.lower()
napis
napis = napis.title() #wszystkie poczatki wyrazow duzymi literami
napis.replace('Ala', 'Tomek')
napis
napis = napis.replace('Ala', 'Tomek')
napis

napis = 'AAAAKupię kota    '
napis.count('A') #ile razy napis A jak input to warto ususnac nadmairowe biale znaki (spacje)
napis = napis.strip() #usuwamy biale znaki spacje tabulacje etc
napis
napis = napis.strip('A')
napis



napis = 'AAAAKupię kota    '
napis.find('z') #szukamy napis z
napis.find('kot')
napis[napis.find('kot')]# przy pomocy klamry mozemy wyciagnac znak konkretny
n = napis.find('k')
napis[n:n+3]

napis = "ala ma kota"
napis = napis.title().replace('Ala', 'Tomek') #łańcuchowanie
napis

