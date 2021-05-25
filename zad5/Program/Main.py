from funkcje import wartosc_funkcji, wzor_funkcji
import numpy as np
import pylab as pb
from aproksymacje import gauss_blad, wsp_wielomian, wart_wielomian
import wielomian


stopien_apro = 0
blad = 0
liczba_wezlow = 0
tab_wsp = []
zmienna_iteracyjna = 1
menu = True
while menu:
    print("""Aproksymowane funkcje:
    1. f(x)=3*x-5
    2. f(x)=|2*x-3|
    3. f(x)=x^4-x^3-x^2-x+1
    4. f(x)=sin(x)
    5. f(x)=cos(x)-x^3
    Q: Zakoncz program
    """)
    wybor = input("Wybor: ").upper()
    if wybor in "12345":
        jest = True
        while jest:
            try:
                liczba_wezlow = int(input("Podaj liczbe wezlow kwadratury Gaussa: "))
                if 1 < liczba_wezlow < 6:
                    jest = False
                else:
                    print("Prosze podac wartosc calkowita z przedzialu <2:5>")
            except ValueError:
                print("Prosze podac wartosc calkowita liczbowa")
        jest = True
        while jest:
            wybor_kryterium = input("""Dokonaj wyboru kryterium aproksymacji: 
1. Kryterium dokladnosci
2. Kryterium stopnia wielomianu aproksymujacego
            """)
            if wybor_kryterium in "2":
                jest2 = True
                while jest2:
                    try:
                        stopien_apro = int(input("Podaj stopien wielomianu aproksymacyjnego: "))
                        if stopien_apro >= 1:
                            jest2 = False
                        else:
                            print("Prosze podac dodatnia wartosc stopnia wielomianu")
                    except ValueError:
                        print("Prosze podac wartosc calowita liczbowa")
                tab_wsp = wsp_wielomian(wybor, liczba_wezlow, stopien_apro)
                jest = False
            elif wybor_kryterium in "1":
                jest2 = True
                while jest2:
                    try:
                        blad = abs(float(input("Podaj oczekiwany maksymaly blad aproksymacji: ")))
                        if blad != 0.0:
                            jest2 = False
                        else:
                            print("Prosze podac wartosc rozna od zera")
                    except ValueError:
                        print("Prosze podac wartosc liczbowa")
                stopien_apro = 1
                dokladnosc = True
                while dokladnosc:
                    tab_wsp = wsp_wielomian(wybor, liczba_wezlow, stopien_apro)
                    if gauss_blad(wybor, stopien_apro, tab_wsp, liczba_wezlow) < blad:
                        dokladnosc = False
                    else:
                        stopien_apro += 1
                jest = False
            else:
                print("Dokonaj prawidlowego wyboru kryterium!")
        arg = np.linspace(-1, 1, 1000)
        pb.plot(arg, wartosc_funkcji(arg, wybor), label='funkcja aproksymowana')
        pb.plot(arg, wart_wielomian(stopien_apro, arg, tab_wsp), label='aproksymacja', linestyle=':')
        pb.xlabel("x")  # opis osi x
        pb.ylabel("y")  # opis osi y
        fig = pb.gcf()
        fig.canvas.set_window_title('Wykres ' + str(zmienna_iteracyjna))
        pb.grid(True)
        pb.legend(loc='upper right')  # tworzy legendę wykresu
        print("Prosze zamknac okno z Wykresem {} aby kontynuowac".format(zmienna_iteracyjna))
        wzor_apro = wielomian.Polynomial(tab_wsp[::-1])
        print("""Wzor wielomianu aproksymacyjnego: 
{}
""".format(wzor_apro))
        print("Blad aproksymacji: {}".format(gauss_blad(wybor, stopien_apro, tab_wsp, liczba_wezlow)))
        pb.title("f(x) = " + str(wzor_funkcji(wybor)))
        pb.show()
        zmienna_iteracyjna += 1
    elif wybor in "Q":
        menu = False
        print("Zakonczenie programu...")
    else:
        print("Dokonaj prawidlowego wyboru")
