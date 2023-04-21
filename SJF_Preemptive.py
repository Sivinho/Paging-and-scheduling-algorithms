#!/usr/bin/env python3

"""SJF Preemptive.py - algorytm SJF Preemptive"""

from os import strerror
import time
start_time = time.time()

print("\nAlgorytm SJF Preemptive\n")

lista_procesow=[]

try:
    procesy=open("procesy.txt","r")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))

linia = procesy.readline().rstrip("\n")
while linia!='':
    lista_procesow.append(linia.split())
    linia = procesy.readline().rstrip("\n")

try:
    procesy.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))

for q in range(len(lista_procesow)):#konwersja czasów przyjścia i czasów wykonywania z łańcucha znaków na liczby całkowite, by móc sortować względem tych wartości
    lista_procesow[q][1] = int(lista_procesow[q][1])
    lista_procesow[q][2] = int(lista_procesow[q][2])

burst_times={}#słownik czasów wykonywania się procesów, aby obliczać końcowe wartości

lista_posortowana = sorted(lista_procesow, key=lambda x: x[1])#sortowanie listy procesów względem czasów przyjścia
kolejka=[]#kolejka procesów gotowych, gdzie proces z samej góry jest już procesem obsługiwanym przez procesor
wt={}#słownik na czasy oczekiwania aż proces będzie się wykonywał po raz ostatni
tat={}#słownik na czasy przetwarzania procesów
completion_time={}#słownik na czasy zakończenia wykonywania procesów
global_time=0#takt procesora
while True:
    length=len(kolejka)
    if lista_posortowana:
        while lista_posortowana[0][1] == global_time:#dodawanie na koniec kolejki procesów, których czas przybycia zgadza się z taktem procesora
            kolejka.append(lista_posortowana[0])
            burst_times[lista_posortowana[0][0]] = lista_posortowana[0][2]
            del lista_posortowana[0]
            if not lista_posortowana:
                break
    if len(kolejka) == 0 and len(lista_posortowana) == 0:#warunek na zakończenie wykonywania się algorytmu
        break
    if len(kolejka) == 0:#warunek gdy procesor jest w stanie uśpienia, nie posiada procesu do wykonywania
        global_time += 1
        continue
    if len(kolejka)!=length:#jeżeli proces w danym takcie procesora został dodany do kolejki, sortuj kolejkę względem czasów wykonywania, proces z najkrótszym czasem wykonywania, będzie obsługiwany przez procesor
        kolejka = sorted(kolejka, key=lambda x: x[2])
    if kolejka[0][2] == 0:#jeżeli czas wykonywania się procesu aktualnie obsługiwanego przez procesor, zakończył się
        completion_time[kolejka[0][0]] = global_time
        tat[kolejka[0][0]] = completion_time[kolejka[0][0]] - kolejka[0][1]
        wt[kolejka[0][0]] = tat[kolejka[0][0]] - burst_times[kolejka[0][0]]
        del burst_times[kolejka[0][0]]
        del kolejka[0]
    if len(kolejka) == 0 and len(lista_posortowana) == 0:
        break
    if len(kolejka) == 0:
        global_time += 1
        continue
    global_time += 1
    kolejka[0][2] -= 1#odjęcie od pozostałego czasu wykonywania się procesu aktualnie obsługiwanego przez procesor
avg_wt=0
avg_tat=0
for klucz in wt.keys():
    print(klucz+" CT:",completion_time[klucz]," TAT:",tat[klucz]," WT:",wt[klucz])
    avg_wt += wt[klucz]
    avg_tat += tat[klucz]
print("Average Turnaround Time=",avg_tat/len(lista_procesow)," Average Waiting Time=",avg_wt/len(lista_procesow))

try:
    wyniki=open("wyniki_algorytmow_szeregowania_procesow.txt","a")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
wyniki.write("Algorytm SJF wywłaszczeniowy\n")
wyniki.write("Średni czas przetwarzania "+str(avg_tat/len(lista_procesow))+" Średni czas oczekiwania "+str(avg_wt/len(lista_procesow))+"\n\n")
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))