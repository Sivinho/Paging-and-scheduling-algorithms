#!/usr/bin/env python3

"""FCFS.py - algorytm FCFS"""

from queue import Queue
from os import strerror

print("\nAlgorytm FCFS\n")

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

lista_posortowana=sorted(lista_procesow,key=lambda x: x[1])#sortowanie listy procesów względem czasów przyjścia
wt={}#słownik na czasy oczekiwania aż proces będzie się wykonywał po raz ostatni
tat={}#słownik na czasy przetwarzania procesów
completion_time={}#słownik na czasy zakończenia wykonywania procesów
global_time=0#takt procesora
burst=0#aktualny czas wykonywania procesu, który obsługuje procesor
kolejka_procesow=Queue()#kolejka procesów gotowych, gdzie proces z samej góry jest już procesem obsługiwanym przez procesor

while True:
    if lista_posortowana:
        while lista_posortowana[0][1] == global_time:#dodawanie na koniec kolejki procesów, których czas przybycia zgadza się z taktem procesora
            kolejka_procesow.put(lista_posortowana[0])
            del lista_posortowana[0]
            if not lista_posortowana:
                break
    if kolejka_procesow.empty() and len(lista_posortowana) == 0:#warunek na zakończenie wykonywania się algorytmu
        break
    if kolejka_procesow.qsize()==0:#warunek gdy procesor jest w stanie uśpienia, nie posiada procesu do wykonywania
        burst=0#wyzerowanie czasu wykonywania procesu aktualnie obsługiwanego przez procesor
        global_time+=1
        continue
    if burst==kolejka_procesow.queue[0][2]:#warunek zakończenia wykonywania się procesu, czyli jeżeli czas wykonywania procesu w procesorze, jest taki sam jak czas wykonywania się tego procesu
        zakonczony=kolejka_procesow.get()#usunięcie procesu z góry i zwrócenie wartości tego procesu
        completion_time[zakonczony[0]]=global_time
        tat[zakonczony[0]]=completion_time[zakonczony[0]]-zakonczony[1]
        wt[zakonczony[0]]=tat[zakonczony[0]]-zakonczony[2]
        burst=0
    if kolejka_procesow.empty() and len(lista_posortowana) == 0:
        break
    if kolejka_procesow.qsize()==0:
        burst=0
        global_time+=1
        continue
    burst+=1
    global_time+=1
avg_wt=0
avg_tat=0
for klucz in wt.keys():
    print(klucz+" CT:",completion_time[klucz]," TAT:",tat[klucz]," WT:",wt[klucz])
    avg_wt += wt[klucz]
    avg_tat += tat[klucz]
print("Średni czas przetwarzania=",avg_tat/len(lista_procesow)," Średni czas oczekiwania=",avg_wt/len(lista_procesow))

try:
    wyniki=open("wyniki_algorytmow_szeregowania_procesow.txt","a")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
wyniki.write("Algorytm FCFS\n")
wyniki.write("Średni czas przetwarzania "+str(avg_tat/len(lista_procesow))+" Średni czas oczekiwania "+str(avg_wt/len(lista_procesow))+"\n\n")
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))