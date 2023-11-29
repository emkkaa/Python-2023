import csv #csv - modul do wczytania tych plikow

with open('data\\foods.csv') as csvfile: #with czyli otwieram plik, z pakietu csv uzywam dictreadera ktory czyta pola z csv jako slownik (ciąg slowników)
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)



# Stwórz czytnik plików CSV bez użycia modułu CSV
#
# napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI - command line interface)
# wypisze jego zawartość oddzielając pola tabulacją \t


import csv
import os
import sys
print(os.getcwd())
tab = '\t'
n = 0
with open(sys.argv[1]) as csvfile:
    for line in csvfile:
        print(f'{n:03d} {tab.join(line.strip().split(","))}')
        n +=1


