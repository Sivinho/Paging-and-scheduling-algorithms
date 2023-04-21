#!/usr/bin/env python3

"""LRU.py - algorytm LRU"""
import ramka
from os import strerror

print("\nAlgorytm LRU\n")

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
recently_used={}#słownik na ostanie użycie danej strony
i=0
for odwolanie in ciag_odwolan:
    if len(ramki)<ramka.ilosc_ramek:
        if odwolanie not in ramki:
            ramki.append(odwolanie)
            recently_used[odwolanie]=i+1
            miss += 1
        else:
            recently_used[odwolanie] = i + 1
    else:
        if odwolanie in ramki:
            recently_used[odwolanie] = i + 1
        else:
            least_recently_used=sorted(recently_used.items(),key=lambda x: x[1])#sortowanie listy krotek powstałej ze słownika ostatnich użyć strony, względem najdawniejszego użycia
            temp = ramki.index(least_recently_used[0][0])#znalezienie w ramkach strony najdawniej używanej
            del ramki[temp]
            del recently_used[least_recently_used[0][0]]
            ramki.insert(temp,odwolanie)
            recently_used[odwolanie] = i + 1
            miss += 1
    i+=1
    #print(i,"Odwolanie: ",ramki)
print("Ilość poprawnych odwołań: ",i-miss)
print("Ilość błędów strony: ",miss)
print("Prawdopodobieństwo wystąpienia błędu strony: ",round(miss/i,2))
print("Procent błędów w odniesieniu do wszystkich odwołań procesora: ",round(miss/i,2)*100,"%")

try:
    wyniki=open("wyniki_algorytmow_zastepowania_stron.txt","a")
    wyniki.write("LRU: "+str(miss) + " ")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))