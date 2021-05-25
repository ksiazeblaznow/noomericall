def horner(lista_wspolczynnikow, arg_x):
    wynik = 0
    for item in lista_wspolczynnikow:    # pobiera współczynniki wielomianu od końca
        wynik = wynik * arg_x + item
    return wynik    # zwrot wartosci wielomianu