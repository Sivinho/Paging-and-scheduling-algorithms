#!/usr/bin/env python3

"""MFU.py - algorytm MFU"""
import ramka
from os import strerror

print("\nAlgorytm MFU\n")

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
            most_frequently_used=sorted(frequency.items(),key=lambda x: x[1],reverse=True)#sortowanie stron w ramce, względem malejącej częstotliwości odwołania
            j=0
            while most_frequently_used[j][0] not in ramki:#pętla która bierze pod uwagę tylko strony znajdujące się w ramkach
                j=j+1
            temp = ramki.index(most_frequently_used[j][0])
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
print("Prawdopodobieństwo wystąpienia błędu strony: ",round(miss/len(ciag_odwolan),2))
print("Procent błędów w odniesieniu do wszystkich odwołań procesora: ",round(miss/len(ciag_odwolan),2)*100,"%")

try:
    wyniki=open("wyniki_algorytmow_zastepowania_stron.txt","a")
    wyniki.write("MFU: "+str(miss) + "\n")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))