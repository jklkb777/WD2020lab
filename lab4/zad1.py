# Zad. 1
# Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku


def create_list():
    return list(range(0,31))

multiplited_list = [element * 2 for element in create_list()]

print(multiplited_list)

plik = open("lab4_zad1.txt", "w")
plik.write(str(multiplited_list))
plik.close()