#!/usr/bin/env python3

"""FIFO.py - algorytm FIFO"""
import ramka
from os import strerror

print("\nAlgorytm FIFO\n")

try:
    odwolania=open("odwolania.txt","r")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))

ciag_odwolan=odwolania.readline().split()

try:
    odwolania.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))

ramki=[]#ramki pamięci fizycznej
miss=0#ilość błędów strony
i=0
for odwolanie in ciag_odwolan:
    if len(ramki)<ramka.ilosc_ramek:
        if odwolanie not in ramki:
            ramki.append(odwolanie)
            miss += 1
        else:
            pass
    else:
        if odwolanie in ramki:
            pass
        else:
            del ramki[0]
            miss+=1
            ramki.append(odwolanie)
    i+=1
print("Ilość poprawnych odwołań: ",i-miss)
print("Ilość błędów strony: ",miss)
print("Prawdopodobieństwo wystąpienia błędu strony: ",round(miss/i,2))
print("Procent błędów w odniesieniu do wszystkich odwołań procesora: ",round(miss/i,2)*100,"%")

try:
    wyniki=open("wyniki_algorytmow_zastepowania_stron.txt","a")
    wyniki.write("Ilość ramek: "+str(ramka.ilosc_ramek)+" FIFO: "+str(miss) +" ")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
