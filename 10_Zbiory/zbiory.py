z = set(range(10))
z
z = {1, 2, 3, 4, 1, 2}
z
z = {'a', 'b', 'c'}
z
'a' in z
'd' in z
'd' not in z
z2 = {'a', 'b', 'c', 'd'}
z < z2
z3 = {'d', 'e'}
z | z3 #suma zbiorów
z & z2
z & z3
z2 - z #mozemy odejmowac zbiory
z2 ^ z3 #roznica symetryczna

z3.add('z') #dodaawanie elementu do zbioru

slownik = {z: 3}  # Błąd to jest zmienne i nie moze byc kluczem w slowniku
fz = frozenset(z) #zamrozony zbior - po zamrozeniu zbior zmianie ulec nie moze
slownik = {fz: 3}
slownik

#błąd TypeError: unhashable type: 'set'
