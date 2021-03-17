import random
# zad 1
# zdefiniuj zbiory w python comprehension

# A = {1-x: x ∈ <1,10>}
# B = {1,4,16,…,4**7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}

# A)
# lista_a = [x-1 for x in range(1, 11)]
# print(lista_a)

# B)
# czworka = 4
# lista_b = [4**x for x in range(0, 8)]
# print(lista_b)
#
# # C)
# lista_c = [x for x in lista_b if x % 2 == 0]
# print(lista_c)


#zad 2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, 
# następnie wykorzystując Python Comprehension zdefiniuj nową listę, 
# która będzie zawierała tylko parzyste elementy
# lista1 = []
# for i in range(10):
#     random_element = random.randint(1, 100)
#     lista1.append(random_element)
# print(lista1)

# lista2 = []
# lista2 = [i for i in lista1 if not (i%2)]
# print(lista2)


# zad 3
# Utwórz słownik z produktami spożywczymi do kupienia. 
# Klucz to niech będzie nazwa produktu a wartość -
# jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, 
# gdzie będą produkty, których wartość to sztuki.

# produkty_spozywcze = {
#     "mleko": "litr",
#     "sok pomarańczowy": "litr",
#     "ziemniaki": "kg",
#     "jabłka": "kg",
#     "mandarynki": "kg",
#     "chleb": "szt",
#     "jajka": "szt"
# }
# produkty_spozywcze2 = []
# produkty_spozywcze2 = [list(produkty_spozywcze.keys())[list(produkty_spozywcze.values()).index("szt")]]

# print(produkty_spozywcze2)

# zad 4
#Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
# def czy_prostokatny(a, b, c):
#     if ((a+b>c) and (a+c>b) and (b+c>a)):
#         if ((a*a+b*b==c*c) or (a*a+c*c==b*b) or (c*c+b*b==a*a)):
#             print("To jest trójkąt prostokątny")
#         else:
#             print("To nie jest trójkąt prostokątny")
#     else:
#         print("Nie można z zbudować trójkąta")
# a = input("Wpisz a: ")
# b = input("Wpisz b: ")
# c = input("Wpisz c: ")
# czy_prostokatny(a, b, c)

# zad 5
#Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne
# def pole_trapezu():
#     a = input("Podaj pierwszą podstawę: ")
#     b = input("Podaj drugą podstawę: ")
#     h = input("Podaj wysokość: ")
#     pole = (int(a) + int(b)) * int(h)/2
#     print(pole)
    
# pole_trapezu()

# zad 6
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), 
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
# def ciag(a = 1, b = 4, ile = 10):
#     i = 0
#     suma = 1
#     for i in range(i, ile):
#         mnozenie = a * b
#         suma *= mnozenie
#     return suma
#
# print(ciag())



# zad 8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci:
# klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.

# produkty = {
#     "mleko": 2.99,
#     "chleb": 2.50,
#     "sok jabłkowy": 3.50,
#     "kasza": 4.20,
#     "żel pod prysznic": 9.99
# }
# #
# def lista_zakupow(**lista_zakupow):
#     ilosc = len(produkty)
#     sum_cena = sum(produkty.values())
    
#     print("Ilość produktów:", ilosc)
#     print("Cena produktów łacznie:", sum_cena,"PLN")

# lista_zakupow()
        
