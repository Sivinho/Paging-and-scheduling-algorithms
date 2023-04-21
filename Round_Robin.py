#!/usr/bin/env python3

"""Round_Robin.py - algorytm Round Robin"""

from queue import Queue
from os import strerror

print("\nAlgorytm Round Robin\n")

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

remaining_burst={}#słownik na pozostałę czasy wykonywania się procesów, aktualizowane z każdym taktem procesora

quantum=int(input("Podaj kwant czasu dla algorytmu Round Robin: "))

lista_posortowana=sorted(lista_procesow,key=lambda x: x[1])#sortowanie listy procesów względem czasów przyjścia
wt={}#słownik na czasy oczekiwania aż proces będzie się wykonywał po raz ostatni
tat={}#słwonik na czasy przetwarzania procesów
ct={}#słownik na czasy zakończenia wykonywania procesów
global_time=0#takt procesora
kolejka_procesow=Queue()#kolejka procesów gotowych, gdzie proces z samej góry jest już procesem obsługiwanym przez procesor
current_burst=0#aktualny czas wykonywania procesu, który obsługuje procesor
while True:
    if lista_posortowana:
        while lista_posortowana[0][1] == global_time:#dodawanie na koniec kolejki procesów, których czas przybycia zgadza się z taktem procesora
            kolejka_procesow.put(lista_posortowana[0])
            remaining_burst[lista_posortowana[0][0]] = lista_posortowana[0][2]
            del lista_posortowana[0]
            if not lista_posortowana:
                break
    if kolejka_procesow.empty() and len(lista_posortowana) == 0:#warunek na zakończenie wykonywania się algorytmu
        break
    if kolejka_procesow.qsize()==0:#warunek gdy procesor jest w stanie uśpienia, nie posiada procesu do wykonywania
        current_burst = 0
        global_time+=1
        continue
    if current_burst==quantum and remaining_burst[kolejka_procesow.queue[0][0]]!=0:#jeżeli czas wykonywania procesu, który aktualnie jest obsługiwany przez procesor jest równy kwantowi, lecz czas jego wykonywania jeszcze się nie skończył
        nakoniec=kolejka_procesow.get()#usunięcie procesu z góry i zwrócenie wartości
        kolejka_procesow.put(nakoniec)#dodanie usuniętego procesu z góry na koniec kolejki
        current_burst=0#wyzerowanie czasu wykonywania procesu aktualnie obsługiwanego przez procesor
    elif current_burst<quantum and remaining_burst[kolejka_procesow.queue[0][0]]==0 or current_burst==quantum and remaining_burst[kolejka_procesow.queue[0][0]]==0:#jeżeli czas wykonywania procesu, który aktualnie jest obsługiwany przez procesor jest mniejszy od kwantu ale proces się zakończył lub czas wykonywania procesu, który aktualnie jest obsługiwany przez procesor jest równy kwantu ale proces się zakończył
        zakonczony = kolejka_procesow.get()#usunięcie procesu z góry i zwrócenie wartości
        ct[zakonczony[0]] = global_time
        tat[zakonczony[0]] = ct[zakonczony[0]] - zakonczony[1]
        wt[zakonczony[0]] = tat[zakonczony[0]] - zakonczony[2]
        del remaining_burst[zakonczony[0]]
        current_burst = 0#wyzerowanie czasu wykonywania procesu aktulanie obsługiwanego przez procesor
    if kolejka_procesow.empty() and len(lista_posortowana) == 0:
        break
    if kolejka_procesow.qsize()==0:
        current_burst=0
        global_time+=1
        continue
    global_time+=1
    current_burst += 1
    remaining_burst[kolejka_procesow.queue[0][0]]-=1#odjęcie od pozostałego czasu wykonywania się procesu aktualnie obsługiwanego przez procesor
avg_wt=0
avg_tat=0
for klucz in wt.keys():
    print(klucz+" CT:",ct[klucz]," TAT:",tat[klucz]," WT:",wt[klucz])
    avg_wt += wt[klucz]
    avg_tat += tat[klucz]
print("Average Turnaround Time=",avg_tat/len(lista_procesow)," Average Waiting Time=",avg_wt/len(lista_procesow))

try:
    wyniki=open("wyniki_algorytmow_szeregowania_procesow.txt","a")
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))
wyniki.write("Algorytm Round Robin\n")
wyniki.write("Średni czas przetwarzania "+str(avg_tat/len(lista_procesow))+" Średni czas oczekiwania "+str(avg_wt/len(lista_procesow))+" Kwant czasu "+str(quantum)+"\n\n")
try:
    wyniki.close()
except Exception as exc:
    print("Błąd: ",strerror(exc.errno))