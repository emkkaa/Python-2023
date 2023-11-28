l = [3, 5, 6, 7]
l

l[1]
l[0]
len(l)
l[0:2]
l[1:2]
l[1:]
l[:2]
l[-1]
l[1:-1]
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd #bo napis 3
l.index(3) #a tu miejsce w indeksie 3 czyli pod jakim indeksem mieszka 3

l[1] = 17
l
del l[3] #usunac element
l
l.append(19) #doklejanie na koncu elementu
l
l += ['A', 'B']
l
l.pop() #zwraca ostatni element z prawej strony listy
l

" - ".join(["Ala", "ma", "kota"])
"".join(["Ala", "ma", "kota"])
" ".join(["Ala", "ma", "kota"])
s2 = '.|.'
s2.join(["Ala", "ma", "kota"])

'.' in s2

#zadanie

napisy = []

while True:
    napis = input("Wprowadź dowolne słowo: ")

    if not napis:
        break

    napisy.append(napis)

print(napisy)
