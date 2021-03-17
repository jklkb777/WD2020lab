# import sys
# from math import *

# zad1
# filmy = ['Zielona mila', 'Skazani na Shawshank', 'Forrest Gump', 'Leon Zawodowiec', 'Requiem dla snu']
# filmy.reverse()
# print(filmy)
# noweFilmy =['Matrix', 'Milczenie owiec', 'Gladiator', 'Avatar', 'Shrek']
# filmy.append(noweFilmy)
# print(filmy)

# zad2
# dataPremiery = {
#     "Matrix" : 1999,
#     "Milczenie owiec" : 1991,
#     "Gladiator" : 2000,
#     "Avatar" : 2009,
#     "Shrek" : 2001
# }

# zad3
# przedmiot = {
#     "Programowanie strukturalne" : "PU",
#     "Komputerowe Wspomaganie Projektowania" : "CAD",
#     "Analiza matematyczna dla informatykow" : "AMDI",
#     "Język angielski" : "JANG",
#     "Wizualizacja danych" : "WD",
#     "Matematyka dyskretna" : "MD"
# }
# ilosc = len(przedmiot)
# print(ilosc)

# zad4
# liczba = float(input("Wprowadz liczbe: "))
# print(pow(liczba,liczba))

# zad5
# file = open("tekst.txt", "w")
# file.write("Ala ma kota")
# file.close()
# file = open("tekst.txt", "r")
# data = (file.readline())
# ilerazy = data.count("a")
# print("Ile razy występuje litera 'a':", ilerazy)

# zad6
# a = int(input("Wprowadz liczbe a: "))
# b = int(input("Wprowadz liczbe b: "))
# c = int(input("Wprowadz liczbe c: "))

# if (a%2==0) & (b>c):
#     print("Liczba", a,"jest parzysta i jednoczesnie", b, "jest większe od", c)
# else:
#      print("Liczba", a,"nie jest parzysta lub", b, "nie jest większe od", c)

# zad7
# lista = [1, 3.14, 6, 7.20]
# for i in range(0, len(lista)):
#     suma = lista[i] + lista[i-1]
#     print(suma)

# zad8
# lista = []
# x = 0
# while x < 10:
#     a = int(input("Wpisz liczbę: "))
#     if (a%2 == 0):
#         lista.append(a)
#     x += 1
# print("\nLista z liczbami parzystymi", lista)

# zad9

# for x in range(0, 1):
#     print('OOOOOO')
#     for i in range(0, 4):
#         print('O    O')
#     print('OOOOOO')

#zad10
try:
    a = int(input("Wpisz numer: "))
    print("Twój podany numer:", a)
except ValueError:
    print("Prosze wpisać liczbę nie słowo!")
