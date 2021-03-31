# zad 1

class Material:
    def __init__(self, nazwa, rodzaj, dlugosc, szerokosc):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(f'Nazwa to: {self.nazwa}')


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo, nazwa, rodzaj, dlugosc, szerokosc):
        super().__init__(nazwa, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(f'Rozmiar: {self.rozmiar}\nKolor: {self.kolor}\nDla kogo: {self.dla_kogo}')


class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, nazwa, rodzaj, dlugosc, szerokosc):
        super().__init__(rozmiar, kolor, dla_kogo, nazwa, rodzaj, dlugosc, szerokosc)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print(self.rodzaj_swetra)


obiekt1 = Ubrania(30,'czerwony','uniseks','koszulka w paski','t-shirt',61,40)
obiekt2 = Sweter('rozpinany','M','czarny','męski','sweter H&M','miękki',70,40)

obiekt1.wyswietl_nazwe()
obiekt1.wyswietl_dane()
print('-'*20)
obiekt2.wyswietl_nazwe()
obiekt2.wyswietl_dane()

# zad 2
# Przeciąż metodę ``__add__()`` dla klasy Kwadrat,
# która będzie zwracała instancje klasy Kwadrat o nowym boku, będącym sumą długości boku kwadratu oraz obwodu kwadratu

class Kwadrat:
    def __init__(self,bok_kwadratu,obwod_kwadratu):
        self.bok_kwadratu = bok_kwadratu
        self.obwod_kwadratu = obwod_kwadratu

    def __add__(self):
        return self.bok_kwadratu + self.obwod_kwadratu


kwadrat1 = Kwadrat(2,8)

print(kwadrat1.__add__())


# Zad. 5

# Za pomocą funkcji `isinstance()` oraz `issubclass()`
# sprawdź wynik dla instancji obiektu `Pracownik` oraz `Menadzer` dla klas `Osoba, Pracownik i Manadzer`.


class Osoba:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja


class Pracownik(Osoba):
    def __init__(self, stanowisko, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko, pensja)
        self.stanowisko = stanowisko


class Menadzer(Osoba):
    def __init__(self, numer_pokoju, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko, pensja)
        self.numer_pokoju = numer_pokoju


alan = Menadzer(12,'Alan','Bąk',5500)
jan = Menadzer(12,'Jan','Kowalski',5000)
ania = Pracownik('spedytor', 'Ania','Malinowska',3500)
mateusz = Pracownik('magazynier','Mateusz','Kalinowski',3000)
beata = Pracownik('sekretarka','Beata','Kępa',3000)

y = isinstance(jan,Pracownik)
x = issubclass(Menadzer,Osoba)
print(f'Czy jan jest instacją Pracownik?: {y}')
print(f'Czy Menadzer jest subklasą Osoba?: {x}')


# Zad. 8

# Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego.
# Zaimplementuj sprawdzanie czy przekazany został string jako argument konstruktora tego iteratora
# (sprawdź funkcję `isinstance()`).


VOWELS = ('a','ą','e','ę','i','o','u','y')

string = input("Wprowadź tekst: ")

res = set([each for each in string if each in VOWELS])


print(f'Wprowadzony tekst: {string}')
print(f'Samogłoski z przekazanego ciągu: {res}')


# Zad. 10

# Napisz generator, który będzie zwracał kolejne wartości ciągu arytmetycznego.


def ciag_arytmetyczny(a,r,n):
    curr_term = a
    for i in range(1, n+1):
        print(curr_term, end=" ")
        curr_term += r


a = int(input('Wprowadż pierwszą liczbę: '))
r = int(input('Wprowadż różnicę: '))
n = int(input('Wprowadż liczbę n-tą '))

ciag_arytmetyczny(a,r,n)