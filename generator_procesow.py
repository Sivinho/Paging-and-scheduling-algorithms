#!/usr/bin/env python3

"""generator_procesow.py - generator danych"""
import numpy
from os import strerror

def generator_z_przedzialu(n,min, max):
    for i in range(n):
        yield numpy.random.randint(min,max+1,1)[0]

def generator_mean_stdev(n,mean,stdev):
    for i in range(n):
        yield abs(numpy.random.normal(mean,stdev,1)[0])


try:
    procesy=open("procesy.txt","w")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))

while True:
    try:
        n=int(input("Podaj liczbę procesów: "))
        assert n>0
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane")
        print("Spróbuj ponownie")
    except AssertionError:
        print("Błąd: Podana liczba jest mniejsza od 1")
        print("Spróbuj ponownie")
    else:
        break


print("Jeżeli chcesz aby czasy przyjścia procesów generowały się z przedziału i czasy wykonywania procesów generowały się z przedziału wybierz: 1")
print("Jeżeli chcesz aby czasy przyjścia procesów generowały się ze średniej oraz odchylenia standardowego i czasy wykonywania procesów generowały się ze średniej oraz odchylenia standardowego wybierz: 2")
print("Jeżeli chcesz aby czasy przyjścia procesów generowały się z przedziału i czasy wykonywania procesów generowały się ze średniej oraz odchylenia standardowego wybierz: 3")
print("Jeżeli chcesz aby czasy przyjścia procesów generowały się ze średniej oraz odchylenia standardowego i czasy wykonywania procesów generowały się z przedziału wybierz: 4")

while True:
    try:
        x=int(input("Podaj swój wybór: "))
        assert x>0 and x<5
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane")
        print("Spróbuj ponownie")
    except AssertionError:
        print("Błąd: Podana liczba nie jest ze zbioru {1,2,3,4}")
        print("Spróbuj ponownie")
    else:
        break
match x:
    case 1:
        while True:
            try:
                min_arrival=int(input("Podaj dolną granicę przedziału czasów przyjścia procesów: "))
                max_arrival=int(input("Podaj górną granicę przedziału czasów przyjścia procesów: "))
                assert min_arrival<=max_arrival and min_arrival>=0 and max_arrival>=0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podana wartość minimum jest mniejsza od 0 lub podana wartość maksimum jest mniejsza od 0 lub minimum jest większe od maksimum")
                print("Spróbuj ponownie")
            else:
                break
        while True:
            try:
                min_burst=int(input("Podaj dolną granicę przedziału czasów wykonywania procesów: "))
                max_burst=int(input("Podaj górną granicę przedziału czasów wykonywania procesów: "))
                assert min_burst<=max_burst and min_burst>0 and max_burst>0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podane wartości są mniejsze od 1 lub minimum jest większe od maksimum")
                print("Spróbuj ponownie")
            else:
                break
        try:
            wyniki = open("wyniki_algorytmow_szeregowania_procesow.txt", "w")
            wyniki.write("Dolna granica przedziału czasów przyjścia procesów "+str(min_arrival)+"\n")
            wyniki.write("Górna granica przedziału czasów przyjścia procesów " + str(max_arrival) + "\n")
            wyniki.write("Dolna granica przedziału czasów wykonywania procesów " + str(min_burst) + "\n")
            wyniki.write("Górna granica przedziału czasów wykonywania procesów " + str(max_burst) + "\n\n")
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        try:
            wyniki.close()
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        for i,j,k in zip(range(n),generator_z_przedzialu(n,min_arrival,max_arrival),generator_z_przedzialu(n,min_burst,max_burst)):
            try:
                procesy.write("P"+str(i+1)+" "+str(j)+" "+str(k)+"\n")
            except IOError as IO:
                print("Błąd I/O: ",strerror(IO.errno))
    case 2:
        while True:
            try:
                mean_arrival = int(input("Podaj średnią czasów przyjścia procesów: "))
                stdev_arrival = float(input("Podaj odchylenie standardowe czasów przyjścia procesów: "))
                assert mean_arrival >= 0 and stdev_arrival >= 0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podane wartości są mniejsze od 0")
                print("Spróbuj ponownie")
            else:
                break
        while True:
            try:
                mean_burst = int(input("Podaj średnią czasów wykonywania procesów: "))
                stdev_burst = float(input("Podaj odchylenie standardowe czasów wykonywania procesów: "))
                assert mean_burst >= 0 and stdev_burst >= 0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podane wartości są mniejsze od 0")
                print("Spróbuj ponownie")
            else:
                break
        try:
            wyniki = open("wyniki_algorytmow_szeregowania_procesow.txt", "w")
            wyniki.write("Średnia czasów przyjścia procesów "+str(mean_arrival)+"\n")
            wyniki.write("Odchylenie standardowe czasów przyjścia procesów " + str(stdev_arrival) + "\n")
            wyniki.write("Średnia czasów wykonywania procesów " + str(mean_burst) + "\n")
            wyniki.write("Odchylenie standardowe czasów przyjścia procesów " + str(stdev_burst) + "\n\n")
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        try:
            wyniki.close()
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        for i, j, k in zip(range(n),generator_mean_stdev(n,mean_arrival,stdev_arrival),generator_mean_stdev(n,mean_burst,stdev_burst)):
            try:
                while round(k)==0:
                    k=abs(numpy.random.normal(mean_burst,stdev_burst,1)[0])
                procesy.write("P" + str(i + 1) + " " + str(round(j)) + " " + str(round(k)) + "\n")
            except IOError as IO:
                print("Błąd I/O: ", strerror(IO.errno))
    case 3:
        while True:
            try:
                min_arrival = int(input("Podaj dolną granicę przedziału czasów przyjścia procesów: "))
                max_arrival = int(input("Podaj górną granicę przedziału czasów przyjścia procesów: "))
                assert min_arrival <= max_arrival and min_arrival >= 0 and max_arrival >= 0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podana wartość minimum jest mniejsza od 0 lub podana wartość maksimum jest mniejsza od 1 lub minimum jest większe od maksimum")
                print("Spróbuj ponownie")
            else:
                break
        while True:
            try:
                mean_burst = int(input("Podaj średnią czasów wykonywania procesów: "))
                stdev_burst = float(input("Podaj odchylenie standardowe czasów wykonywania procesów: "))
                assert mean_burst >= 0 and stdev_burst >= 0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podane wartości są mniejsze od 0")
                print("Spróbuj ponownie")
            else:
                break
        try:
            wyniki = open("wyniki_algorytmow_szeregowania_procesow.txt", "w")
            wyniki.write("Dolna granica przedziału czasów przyjścia procesów " + str(min_arrival) + "\n")
            wyniki.write("Górna granica przedziału czasów przyjścia procesów " + str(max_arrival) + "\n")
            wyniki.write("Średnia czasów wykonywania procesów " + str(mean_burst) + "\n")
            wyniki.write("Odchylenie standardowe czasów przyjścia procesów " + str(stdev_burst) + "\n\n")
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        try:
            wyniki.close()
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        for i, j, k in zip(range(n),generator_z_przedzialu(n,min_arrival,max_arrival),generator_mean_stdev(n,mean_burst,stdev_burst)):
            try:
                while round(k)==0:
                    k=abs(numpy.random.normal(mean_burst,stdev_burst,1)[0])
                procesy.write("P" + str(i + 1) + " " + str(j) + " " + str(round(k)) + "\n")
            except IOError as IO:
                print("Błąd I/O: ", strerror(IO.errno))
    case 4:
        while True:
            try:
                mean_arrival = int(input("Podaj średnią czasów przyjścia procesów: "))
                stdev_arrival = float(input("Podaj odchylenie standardowe czasów przyjścia procesów: "))
                assert mean_arrival >= 0 and stdev_arrival >= 0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podane wartości są mniejsze od 0")
                print("Spróbuj ponownie")
            else:
                break
        while True:
            try:
                min_burst=int(input("Podaj dolną granicę przedziału czasów wykonywania procesów: "))
                max_burst=int(input("Podaj górną granicę przedziału czasów wykonywania procesów: "))
                assert min_burst<=max_burst and min_burst>0 and max_burst>0
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane")
                print("Spróbuj ponownie")
            except AssertionError:
                print("Błąd: Podane wartości są mniejsze od 1 lub minimum jest większe od maksimum")
                print("Spróbuj ponownie")
            else:
                break
        try:
            wyniki = open("wyniki_algorytmow_szeregowania_procesow.txt", "w")
            wyniki.write("Średnia czasów przyjścia procesów " + str(mean_arrival) + "\n")
            wyniki.write("Odchylenie standardowe czasów przyjścia procesów " + str(stdev_arrival) + "\n")
            wyniki.write("Dolna granica przedziału czasów wykonywania procesów " + str(min_burst) + "\n")
            wyniki.write("Górna granica przedziału czasów wykonywania procesów " + str(max_burst) + "\n\n")
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        try:
            wyniki.close()
        except Exception as exc:
            print("Błąd: ", strerror(exc.errno))
        for i, j, k in zip(range(n),generator_mean_stdev(n,mean_arrival,stdev_arrival),generator_z_przedzialu(n,min_burst,max_burst)):
            try:
                procesy.write("P" + str(i + 1) + " " + str(round(j)) + " " + str(k) + "\n")
            except IOError as IO:
                print("Błąd I/O: ", strerror(IO.errno))
try:
    procesy.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))