while True:
    try:
        ilosc_ramek = int(input("Podaj liczbę ramek dla algorytmów: "))
        assert ilosc_ramek > 0
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane")
        print("Spróbuj ponownie")
    except AssertionError:
        print("Błąd: Podana liczba nie jest większa od 0")
        print("Spróbuj ponownie")
    else:
        break