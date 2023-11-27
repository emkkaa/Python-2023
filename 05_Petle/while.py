n = 5

while n > 0:
    print(n)
    n -= 1 #od n odejmuje 1

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')



    #zadanie

    i = int(input("podaj liczbę naturalną"))
    suma_cyfr = (i % 10 + i // 10)
    if (suma_cyfr % 7 == 0) and (i % 2 == 0):
        print('Dobra liczba')
    else:
        print('Zła liczba')

i=0
while i<100:
    i+=1
    if i % 2 == 0 and (i % 10 + i // 10) % 7 == 0:
        print(i)
        continue
else:
    print('Koniec')

    i = int(input("podaj liczbę naturalną"))
    while i % 10 + i // 10:
        print('Liczba')


liczba = input("Podaj liczbe")

suma_liczb = 0
for g in liczba:

    suma_liczb += int(g)

print(f"suma liczby{liczba} wynosi:{suma_liczb}")




n = int(input("Podaj liczbę:"))
print(f'Podałeś liczbę {n}')

suma = 0
while n > 0:
    suma += n % 10
    n //= 10

print(suma)