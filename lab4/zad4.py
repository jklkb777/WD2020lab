#  Zad.4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# •	nazwa_produktu, ilosc, jednostka_miary, cena_jed
# •	oraz metody:
# •	konstruktor – który nadaje wartości
# •	wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# •	ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# •	ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
        return str(self.ilosc), (self.jednostka_miary)

    def ile_kosztuje(self):
        return int(self.ilosc * self.cena_jed)


ziemniaki = NaZakupy("ziemniaki", 10, "kg", 1)
woda = NaZakupy("woda", 1.5, "l", 2.20)

print(ziemniaki.ile_kosztuje())

print(ziemniaki.ile_produktu())
ziemniaki.wyswietl_produkt()
