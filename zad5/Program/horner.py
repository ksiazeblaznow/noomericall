def horner(lista_wspolczynnikow, arg_x):
    """Zwracanie wartości wybranego wielomianu z użyciem schematu Hornera

            Parametry
            ----------
            lista_wspolczynnikow : int list
                wartości współczynników wielomianu zapisane w liście
                w kolejności od stojącego od wyrazu wolnego do najwyższej potęgi
            x : float
                argument dla którego obliczamy wartość funkcji
            Dane wyjsciowe
            -------
            wynik : float
                wynik obliczeń
    """
    wynik = 0
    for item in lista_wspolczynnikow:    # pobiera współczynniki wielomianu od końca
        wynik = wynik * arg_x + item
    return wynik    # zwrot wartosci wielomianu