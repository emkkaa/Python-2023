class Employee: #tworze pusta klase employee
    pass


john = Employee()

john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

john.salary #nie hcemy zeby kazdy widzial to salary, zarobki


class Employee:
    def __init__(self, name, dept, salary):#konstruktor init na wejsciu musi dostac name, dept, salary
        self.__name = name
        self.__dept = dept
        self.__salary = salary #__nazwa pole prywatne, sygnalizacja braku dostepu przez __ dwa podkreslenia

    def get_salary(self):
        return self.__salary


john = Employee('John Doe', 'computer lab', 1000)
john.__salary  # error

john.get_salary()

john._Employee__salary

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property #dekoratory pythona
    def r(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


p = Point(3.0, 4.0)
p
print(p.r) #tutaj za kazdym razem wywolujemy funkcje, przez tą kropke
p.r = 7  # error

# Anatomia obiektu

print(p.__dict__) #obiekt jest slownikiem, slownik to jest wnetrze obiektu
print(Point.__dict__) #wszelkie funkcje mieszkaja w klasie (klasa mowi jaka obiekt ma funkcjonalnosc)
