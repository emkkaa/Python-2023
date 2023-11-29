import json #Javascript object notation pozwala zamienic arbitralna strukture danych nanapis i jak ktos to dostanie to jest w stanie odtworzyc te strukture danych

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

s = json.dumps(data) #bierzde dane i zamienia nna stringa dump string zmiana struktury danych pytonskich na napis bo latwiej przerzucic przez siec
print(s)
print(len(s))
print(type(s))
print()
data = json.loads(s) #przerzucan dane przez siec i odbieram je loads
print(data)
print(len(data))
print(type(data))