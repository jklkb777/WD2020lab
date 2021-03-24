# Zad 5
# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#
# •	wyświetl_dane – drukuje elementy na ekran
# •	pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# •	pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# •	policz_sume – liczy sume elementow
# •	policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
#
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class CiagiArytmetyczne():
    def __init__(self, a1, n, r):
        self.a1 = a1
        self.n = n
        self.r = r


    def pobierz_elementy(self):
        an = self.a1 + (self.n - 1) * self.r
        return an

    @classmethod
    def pobierz_parametry(self):
        self.a1 = input("Podaj wyraz pierwszy: ")
        self.n = input("Podaj liczbę elementów: ")
        self.r = input("Podaj roznice ciągu: ")
        return self.a1, self.n, self.r

    def wyswietl_dane(self):
        print(self.a1), (self.n), (self.r)

    def policz_sume(self):

        return int((self.a1 + self.pobierz_elementy() / 2) * self.n)

    def policz_elementy(self):
        i = 2
        az = self.a1 + self.r
        print("a1 = ", self.n)
        for i in range(self.n):
            print("a" + str(i) + " = " + az)
            az += self.n


ciag = CiagiArytmetyczne.pobierz_parametry()

CiagiArytmetyczne.wyswietl_dane(ciag)