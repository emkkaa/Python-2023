s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'} #pod kluczem a jest 1 pod kluczem b jest 2
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a') #zwroci nic jak nic nie znajdzie a jak znajdzie to zwroci wartosc
s.get('c', 0)
s['c'] = 3
s
del s['b'] #usunac ze slownika
s

s = {"a": 1, 'b': 2, 'c': 3}
#mozemy iterowac po kluczach
for k in s.keys():
    print(k)
#mozemy iterowac po wartosciach
for k in s.values():
    print(k)
#po pozycjach (itemach - itemem jest krotka)
for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s|s2 #dodawanie slownikow

s|={'e':5} #jak plus dla slownikow - belka pionowa
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]} #klucze slownikow - liczba, napis, krotka (na dzis)


#Zadanie1

l = []
d = {}
while True:
    napis = input("Podaj napis, a dodam go do listy: ").strip()
    if napis == "":
        break
    l.append(napis)
#l = ['Ala', 'ma', 'kota', 'kota']
for i in l:
    if d.get(i, 0) == 0:
        d[i]=1
    else:
        print (i)
        d[i] += 1
print(f"Tak się sprawy mają: {d}")

licznik = d.get(i,0)
licznik+=1
d[i] = licznik

#Zadanie2

jednosci = {0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć", 10: "dziesięć"} #modulo 10
dziesiatki  = #modulo 100/ bez reszty przez 10
setki =
liczba = input("Podaj liczbę:")

########
jednostka = jednosci[liczba % 10]
    dziesiatka = dziesiatki[(liczba // 10) % 10]
    nastka = nastki[liczba % 100] if 10 < liczba % 100 < 20 else ""
    setka = setki[(liczba // 100) % 10]


