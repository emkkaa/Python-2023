l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')
except IndexError as e:
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")


# wczytaj przy użyciu input liczbę; wypisz sumę jej cyfr; jeśli podano błędne wejście, poproś jeszcze raz


liczba = 0
while True:
    try: liczba = input("Podaj liczbę naturalną: ")
    liczba = int(liczba)
    except ValueError as e:
    print (f"{liczba} nie jest liczbą!")
    else:
        break
    suma = 0
    i = liczba
    while i > 0:
        suma += i%10 i //= 10
        print (f'Suma cyfr podanej liczby {liczba} wynosi {suma}')

##################################
try:
    n = int(input("Podaj liczbę:"))
    print(f'Podałeś liczbę {n}')

suma = 0
while n > 0:
    suma += n % 10
    n //= 10

print(suma)