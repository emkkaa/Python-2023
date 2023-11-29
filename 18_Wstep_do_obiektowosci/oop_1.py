class MyClass:
    i = 12345 #to jest pole ktore prznalezy do klasy, pole klasy nalezace do wszystkich, taki rekord osobowy

    def __init__(self, n): #(parametr n to jest ta jedynka w 11 linii)
        self.n = n

    def f(self):
        return f'hello world {self.n}'


o1 = MyClass(1) #obiekt = nazwa klasy + parametry przekazywane do kostruktora
o2 = MyClass(2)

o1

o1.i
o2.i
o1.n
o2.n
o1.f()
o2.f()


class MyClass:
    i = 0

    def __init__(self, n):
        self.i+=1
        self.n = n

    def f(self):
        print(self)
        return f'hello world {self.n}'

    @classmethod
    def get_i(cls):
        print(cls)
        return cls.i

o1 = MyClass(1)
o2 = MyClass(2)

o1.i
o2.i
o1.n
o2.n
o1.f()
o2.get_i()


