from funkcje import func


# wspolczynniki arbitralnie wyznaczone, wielomiany Legendre'a
def wspolczynniki(liczba_wezlow, numer_wezla):
    dane = (
        ((- 0.577350, 1), (0.577350, 1)),
        ((- 0.774597, 5 / 9), (0, 8 / 9), (0.774597, 5 / 9)),
        ((- 0.861136, 0.347855), (- 0.339981, 0.652145), (0.339981, 0.652145), (0.861136, 0.347855)),
        ((- 0.906180, 0.236927), (- 0.538469, 0.478629), (0, 0.568889), (0.538469, 0.478629), (0.906180, 0.236927))
    )
    return dane[liczba_wezlow - 2][numer_wezla]


# stopień wielomianu, argument funkcji
# zwraca wartość funkcji bazowej Legendre'a dla x stopnia k
def base_func(degree, x):
    p = [1, x]
    for n in range(2, degree + 1):
        p.append(((2 * (n - 1) + 1) / n * x * p[n - 1] - (n - 1) / n * p[n - 2]))
    return p[degree]


# Liczy całkę
# func_choice: wybór dostępnej funkcji (String)
# liczba_wezlow: liczba węzłów (int)
# k: stopień wielomianu aproksymującego (int)
# zwraca wartość kwadratury w liczniku
def gauss_licznik(func_choice, liczba_wezlow, k):
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * func(x, func_choice) * base_func(k, x)
    return calka


# func_choice: wybór dostępnej funkcji (String)
# k: stopień wielomianu aproksymującego (int)
# tab_wsp: lista współczynników wielomianu aproksymującego
# liczba_wezlow: liczba węzłów kwadratury (int)
# zwraca wartość całki oznaczająca błąd aproksymacji
def gauss_blad(func_choice, k, tab_wsp, liczba_wezlow):
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        # x = - 1 + 2 * (x - a)/(b - a)
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * (func(x, func_choice) - wart_wielomian(k, x, tab_wsp))**2
    return calka

# func_choice: wybór dostępnej funkcji (String)
# zwraca wspołczynnik wielomianu aproksymujacego
def wsp_apro(func_choice, liczba_wezlow, k):
    wsp = (2 * k + 1) / 2 * gauss_licznik(func_choice, liczba_wezlow, k)
    return wsp


# :param func_choice: wybór dostępnej funkcji (String)
# zwraca lista wspołczynników wielomianu aproksymującego
def wsp_wielomian(func_choice, liczba_wezlow, k):
    wielomian = []
    for i in range(k + 1):
        wielomian.append(wsp_apro(func_choice, liczba_wezlow, i))
    return wielomian


# :param k: -//-
# :param x: -//-
# :param tab_wsp: -//-
# zwraca wartość wielomianu aproksymującego dla argumentu x
def wart_wielomian(k, x, tab_wsp):
    poly = 0
    for i in range(k + 1):
        poly += tab_wsp[i] * base_func(i, x)
    return poly
