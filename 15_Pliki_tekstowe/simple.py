f = open('README.md', encoding='utf8') #to f to jest deskryptor pliku to jest plik z ktorego bede czytac

n = 0

for line in f: # w petli for jade po f, pod line jedna linia tekstu, plik tekstowy podzielony na linie wiec wczytuje sie go linia po linii (iterator z f)
    print(f'{n:03d} {line.strip()}')
    n += 1
