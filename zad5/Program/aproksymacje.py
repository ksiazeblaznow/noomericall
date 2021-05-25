from funkcje import wartosc_funkcji


def wspolczynniki(liczba_wezlow, numer_wezla):
    """
    :param liczba_wezlow: liczba węzłów (int)
    :param numer_wezla: numer węzła (int)
    :return: para liczb: (wartość w węźle, waga)
    """
    dane = (
        ((- 0.577350, 1), (0.577350, 1)),
        ((- 0.774597, 5 / 9), (0, 8 / 9), (0.774597, 5 / 9)),
        ((- 0.861136, 0.347855), (- 0.339981, 0.652145), (0.339981, 0.652145), (0.861136, 0.347855)),
        ((- 0.906180, 0.236927), (- 0.538469, 0.478629), (0, 0.568889), (0.538469, 0.478629), (0.906180, 0.236927))
    )
    return dane[liczba_wezlow - 2][numer_wezla]


def funkcja_bazowa(k, x):
    """
    :param k: stopień wielomianu (int)
    :param x: argument funkcji (float)
    :return: wartość funkcji bazowej Legendre'a dla x stopnia k
    """
    p = [1, x]
    for n in range(2, k + 1):
        p.append(((2 * (n - 1) + 1) / n * x * p[n - 1] - (n - 1) / n * p[n - 2]))
    return p[k]


def gauss_licznik(wybor_funkcji, liczba_wezlow, k):
    """
    Obliczanie całki występującej we wzorze na współczynnik wielomianu aproksymującego w liczniku
    :param wybor_funkcji: wybór dostępnej funkcji (String)
    :param liczba_wezlow: liczba węzłów (int)
    :param k: stopień wielomianu aproksymującego (int)
    :return: wartość kwadratury w liczniku
    """
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * wartosc_funkcji(x, wybor_funkcji) * funkcja_bazowa(k, x)
    return calka


def gauss_blad(wybor_funkcji, k, tab_wsp, liczba_wezlow):
    """
    :param wybor_funkcji: -//-
    :param k: stopień wielomianu aproksymującego (int)
    :param tab_wsp: lista współczynników wielomianu aproksymującego
    :param liczba_wezlow: liczba węzłów kwadratury (int)
    :return: wartość całki oznaczająca błąd aproksymacji
    """
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        # x = - 1 + 2 * (x - a)/(b - a)
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * (wartosc_funkcji(x, wybor_funkcji) - wart_wielomian(k, x, tab_wsp))**2
    return calka


def wsp_apro(wybor_funkcji, liczba_wezlow, k):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param k: -//-
    :return: wspołczynnik wielomianu aproksymujacego
    """
    wsp = (2 * k + 1) / 2 * gauss_licznik(wybor_funkcji, liczba_wezlow, k)
    return wsp


def wsp_wielomian(wybor_funkcji, liczba_wezlow, k):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param k: -//-
    :return: lista wspołczynników wielomianu aproksymującego
    """
    wielomian = []
    for i in range(k + 1):
        wielomian.append(wsp_apro(wybor_funkcji, liczba_wezlow, i))
    return wielomian


def wart_wielomian(k, x, tab_wsp):
    """
    :param k: -//-
    :param x: -//-
    :param tab_wsp: -//-
    :return: wartość wielomianu aproksymującego dla argumentu x
    """
    poly = 0
    for i in range(k + 1):
        poly += tab_wsp[i] * funkcja_bazowa(i, x)
    return poly
