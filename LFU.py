#!/usr/bin/env python3

"""LFU.py - algorytm LFU"""
import ramka
from os import strerror

print("\nAlgorytm LFU\n")

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
frequency={}#słownik częstotliwości odwołania danych stron
i=0
for odwolanie in ciag_odwolan:
    if len(ramki)<ramka.ilosc_ramek:
        if odwolanie not in ramki:
            ramki.append(odwolanie)
            frequency[odwolanie]=1
            miss += 1
        else:
            frequency[odwolanie] += 1
    else:
        if odwolanie in ramki:
            frequency[odwolanie] += 1
        else:
            least_frequently_used=sorted(frequency.items(),key=lambda x: x[1])#sortowanie stron w ramce, względem rosnącej częstotliwości odwołania
            j=0
            while least_frequently_used[j][0] not in ramki:#pętla która bierze pod uwagę tylko strony znajdujące się w ramkach
                j=j+1
            temp = ramki.index(least_frequently_used[j][0])#znalezienie w ramce strony najczęściej używanej
            del ramki[temp]
            ramki.insert(temp, odwolanie)
            if odwolanie not in frequency.keys():
                frequency[odwolanie] = 1
            else:
                frequency[odwolanie] += 1
            miss += 1
    i+=1
print("Ilość poprawnych odwołań: ",i-miss)
print("Ilość błędów strony: ",miss)
print("Prawdopodobieństwo wystąpienia błędu strony: ",round(miss/i,2))
print("Procent błędów w odniesieniu do wszystkich odwołań procesora: ",round(miss/i,2)*100,"%")

try:
    wyniki=open("wyniki_algorytmow_zastepowania_stron.txt","a")
    wyniki.write("LFU: "+str(miss) + " ")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))