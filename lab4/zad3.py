# Zad. 3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

with open("lab4_zad1.txt", "r") as plik:
    for linia in plik:
        print(linia, "test\nala ma kota\npython jest super")