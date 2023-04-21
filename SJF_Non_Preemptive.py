#!/usr/bin/env python3

"""SJF Non Preemptive.py - algorytm SJF Non Preemptive"""

from os import strerror

print("\nAlgorytm SJF Non Preemptive\n")

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


lista_posortowana = sorted(lista_procesow, key=lambda x: x[1])#sortowanie listy procesów względem czasów przyjścia
kolejka=[]#kolejka procesów gotowych, gdzie proces z samej góry jest już procesem obsługiwanym przez procesor
wt={}#słownik na czasy oczekiwania aż proces będzie się wykonywał po raz ostatni
tat={}#słownik na czasy przetwarzania procesów
completion_time={}#słownik na czasy zakończenia wykonywania procesów
burst=0#aktualny czas wykonywania procesu, który obsługuje procesor
global_time=0#takt procesora
while True:
    if lista_posortowana:#jeżeli lista niepusta
        i = 0
        while lista_posortowana[i][1] == global_time:#pętla zliczająca ilośc procesów o tym samym czasie przyjścia
            i += 1
            if not lista_posortowana[i:]:
                break
        if i == 1:
            kolejka.append(lista_posortowana[0])
            del lista_posortowana[0]
        elif i>1:#jeżeli procesów o tym samym czasie przyjścia jest więcej niż 1, dodajemy je do kolejki względem czasu wykonania
            temporary_lista = []
            for j in range(i):
                temporary_lista.append(lista_posortowana[0])
                del lista_posortowana[0]
            temporary_lista = sorted(temporary_lista, key=lambda x: x[2])
            for proces in temporary_lista:
                kolejka.append(proces)
            del temporary_lista
    if len(kolejka) == 0 and len(lista_posortowana) == 0:#warunek na zakończenie wykonywania się algorytmu
        break
    if len(kolejka) == 0:#warunek gdy procesor jest w stanie uśpienia, nie posiada procesu do wykonywania
        burst = 0#wyzerowanie czasu wykonywania procesu aktualnie obsługiwanego przez procesor
        global_time += 1
        continue
    if burst == kolejka[0][2]:#warunek zakończenia wykonywania się procesu, czyli jeżeli czas wykonywania procesu w procesorze, jest taki sam jak czas wykonywania się tego procesu
        completion_time[kolejka[0][0]] = global_time
        tat[kolejka[0][0]] = completion_time[kolejka[0][0]] - kolejka[0][1]
        wt[kolejka[0][0]] = tat[kolejka[0][0]] - kolejka[0][2]
        del kolejka[0]
        kolejka = sorted(kolejka, key=lambda x: x[2])#sortowanie kolejki względem czasów wykonywania
        burst = 0
    if len(kolejka) == 0 and len(lista_posortowana) == 0:
        break
    if len(kolejka) == 0:
        burst = 0
        global_time += 1
        continue
    burst += 1
    global_time += 1
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
wyniki.write("Algorytm SJF nie wywłaszczeniowy\n")
wyniki.write("Średni czas przetwarzania "+str(avg_tat/len(lista_procesow))+" Średni czas oczekiwania "+str(avg_wt/len(lista_procesow))+"\n\n")
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))