import numpy
from os import strerror
def generator_z_przedzialu(n,min, max):
    for i in range(n):
        yield numpy.random.randint(min,max+1,1)[0]
try:
    odwolania = open("odwolania.txt", "w")
except Exception as exc:
    print("Błąd: ", strerror(exc.errno))

while True:
    try:
        n = int(input("Podaj liczbę odwołań: "))
        assert n > 0
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane")
        print("Spróbuj ponownie")
    except AssertionError:
        print("Błąd: Podana liczba jest mniejsza od 1")
        print("Spróbuj ponownie")
    else:
        break

while True:
    try:
        ilosc_stron = int(input("Podaj ilość stron: "))
        assert ilosc_stron > 0
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane")
        print("Spróbuj ponownie")
    except AssertionError:
        print("Błąd: Podana wartość liczby stron jest mniejsza od 1")
        print("Spróbuj ponownie")
    else:
        break

try:
    wyniki=open("wyniki_algorytmow_zastepowania_stron.txt","w")
    wyniki.write("Ilość stron " + str(ilosc_stron) + "\n")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))


for i in generator_z_przedzialu(n, 1, ilosc_stron):
    odwolania.write(str(i) + " ")

try:
    odwolania.close()
except Exception as exc:
    print("Błąd: ", strerror(exc.errno))