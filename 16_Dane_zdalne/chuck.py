import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"
response = requests.request(method="GET", url=url)  #response - obiekt z bardzo duza iloscia pól, klucze, kodowania, json to ciało odpowiedzi

pprint(response.json())

print()
print(25*"*")
print()
print(response.json()['value'])



# Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true; Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)

import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)

pprint(response.json())
print()

powierzchnia = response.json()[0]['area']
ludnosc = response.json()[0]['population']
print(f'Powierzchnia: {powierzchnia} km2')
print(response.json()[0]['area'])
print(response.json()[0]['population'])
print(response.json()[0]['currencies'])