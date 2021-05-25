from funkcje import func, func_str
import numpy as np
import pylab as pb
from aproksymacje import gauss_blad, wsp_wielomian, wart_wielomian
import wielomian


approx_degree = 0
err = 0.0
nodes = 0
coeff_array = []  # tablica wspolycznnikow wielomianu apoksymujacego
iter = 1
menu = True  # flaga menu

while menu:
    print("Wybierz funkcję aproksymowaną na przedziale <-1:1>")
    print("1. f(x)=3*x-3")
    print("2. f(x)=|2*x-1|")
    print("3. f(x)=x^4-x^3-x^2-x+1")
    print("4. f(x)=sin(x)")
    print("5. f(x)=cos(x)-x^4")
    print("Q: Zakoncz program")

    wybor = input("> ").upper()
    if wybor in "12345":

        while nodes > 6 or nodes < 1:
            nodes = int(input("Liczba wezlow kwadratury Gaussa: "))

        flag = True
        while flag:
            print("Wybierz kryterium aproksymacji:")
            print("1. Kryterium dokladnosci")
            print("2. Kryterium stopnia wielomianu aproksymujacego")
            wybor_kryterium = input("")

            if wybor_kryterium in "2":
                while approx_degree < 1:
                    approx_degree = int(input("Podaj stopien wielomianu aproksymacyjnego: "))
                coeff_array = wsp_wielomian(wybor, nodes, approx_degree)
                flag = False

            elif wybor_kryterium in "1":
                while err == 0:
                    err = abs(float(input("Podaj oczekiwany maksymaly blad aproksymacji: ")))
                approx_degree = 1
                dokladnosc = True

                while dokladnosc:
                    coeff_array = wsp_wielomian(wybor, nodes, approx_degree)
                    if gauss_blad(wybor, approx_degree, coeff_array, nodes) < err:
                        dokladnosc = False
                    else:
                        approx_degree += 1
                flag = False
            else:
                print("Bledne kryterium")

        # Poniżej wyliczanie wartości i
        # tworzenie wykresu
        args = np.linspace(-1, 1, 1000)

        pb.plot(args, func(args, wybor), label='funkcja aproksymowana')
        pb.plot(args, wart_wielomian(approx_degree, args, coeff_array), label='aproksymacja', linestyle=':')
        pb.xlabel("x")  # opis osi x
        pb.ylabel("y")  # opis osi y

        fig = pb.gcf()  # bierze aktualny wykres
        fig.canvas.set_window_title('Wykres ' + str(iter))

        pb.grid(True)
        pb.legend(loc='upper right')  # tworzy legendę wykresu

        wzor_apro = wielomian.Polynomial(coeff_array[::-1])
        print("""Wzor wielomianu aproksymacyjnego:
{}
""".format(wzor_apro))
        print("Blad aproksymacji: {}".format(gauss_blad(wybor, approx_degree, coeff_array, nodes)))
        pb.title("f(x) = " + str(func_str(wybor)))
        pb.show()
        approx_degree = 0
        iter += 1
    elif wybor in "Q":
        menu = False
        print("Naura")
