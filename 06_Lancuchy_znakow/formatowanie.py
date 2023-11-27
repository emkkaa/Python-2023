s = 'Ala ma {0} kotów'.format(5)
s

'Ala ma ' + str(5) + ' kotów'

s = 'Ala ma {0} kot{1}'.format(5, 'ów') #pierwsza wartosc liczba druga to koncowka odmiany
s

s = 'Ala ma {0} kot{1}'.format(4, 'y')
s

f'Pi to jest mniej więcej {3.1415926:.3}' #wszystko co jest wtedy w wasach to traktowane jest jako kod pythona

for i in range(12):
    print(f'{i:2}') # ja chce zeby kazda z tych liczb zajmowala dwa zaki (dwa miejsca)

for i in range(12):
    print(f'{i:02}')

from math import pi
pi

f'{pi:.3}'
f'{pi:.3f}'
f'{pi-3:.3f}' #float
f'{12:3d}'#cyfry dziesietne
f'{12:03d}'
f'{pi:<30.2f}' #2 znaki po przeciku wyjustowane do lewej strony
f'{pi:>30.2f}'#wyjustowane do prawej
f'{pi:->30.2f}'
f'{pi:^30.2f}'# wycentrowane
f'{"-"*10}HELLO{"-"*10}'
f'{"HELLO":-^25s}'


#zadanie

g = f'{"*":*^1s}'


liczba = input("Podaj liczbe")

while liczba=7:
    liczba+=
        print(i)
        continue
else:
    print('Koniec')

if n = 7:
    break
print(f'{n} tak')


wysokosc = int (input("Podaj wysokość choinki: "))
szerokosc = 1
for i in range (wysokosc):
    print (f'{"*"*szerokosc:^{wysokosc*2}}')
    szerokosc += 2
print (f'{"*":^{wysokosc*2}}')
print (f'{"***":^{wysokosc*2}}')
