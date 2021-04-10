import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from icecream import ic
import expertorium as exp

window = tk.Tk()


# funkcje gui
def click():
    ic(function.get(), method.get(), epsilon.get(), aEntry.get(), bEntry.get() )  # TODO
    
    if not exp.is_float(epsilon.get()):
        tk.messagebox.showinfo(title="Halo", message="Epsilon musi być wartością zmiennoprzecinkową (double)")
        return 0
    elif not exp.is_int(iterations.get()):
        tk.messagebox.showinfo(title="Halo", message="Liczba iteracji to wartość całkowita")
        return 0
    elif not exp.is_int(aEntry.get()):
        tk.messagebox.showinfo(title="Halo", message="Poczatkowa granica przedzialu powinna byc wartoscia int")
        return 0
    elif not exp.is_int(bEntry.get()):
        tk.messagebox.showinfo(title="Halo", message="Koncowa granica przedzialu powinna byc wartoscia int")
        return 0
    else:
        eps = float(epsilon.get())
        iters = int(iterations.get())
        x0 = 0
        if method.get() == 1:
            x0 = (exp.bisection(granice[0], granice[1], eps, iters, function.get()))
            print("Bisekcja:", round(x0, 4))
        elif method.get() == 2:
            x0 = exp.falsi(granice[0], granice[1], eps, iters, function.get())
            print("Regula Falsi:")
            print(round(x0, 4)) #miejsce zerowe reguly Falsi w konsoli, zeby widziec czy wgl to dziala
        else:
            tk.messagebox.showerror(message="Method range out of bounds")

        exp.make_plot( int(aEntry.get()), int(bEntry.get()), [x0, exp.f(x0, function.get())], function.get() )


# zmienne
method = tk.IntVar(window, 1)
function = tk.IntVar(window, 1)

granice = [-10, 10]  # TODO chwilowo są na stałe

# gui
app_bg = '#005348'
window['bg'] = app_bg

label = tk.Label(window, bg=app_bg, fg="white",text="Fabryka miejsc zerowych", font=("Caviar Dreams", 30)).pack(padx=100, pady=50)
functions = tk.Frame( window, bg=app_bg )  # choose function
tk.Radiobutton(window, text = "x^3 + 3*x^2 - x + 10", variable = function, value = 1, indicator = 0, background = app_bg).pack(side=tk.LEFT, in_=functions, padx=10, pady=10)
tk.Radiobutton(window, text = "sin(x)", variable = function, value = 2, indicator = 0, background = app_bg).pack(side=tk.LEFT, in_=functions, padx=10, pady=10)
tk.Radiobutton(window, text = "3^x - 30", variable = function, value = 3, indicator = 0, background = app_bg).pack(side=tk.LEFT, in_=functions, padx=10, pady=10)
tk.Radiobutton(window, text = "cos(x) + x^3 - 19", variable = function, value = 4, indicator = 0, background = app_bg).pack(side=tk.LEFT, in_=functions, padx=10, pady=10)
functions.pack()
methods = tk.Frame( window, bg=app_bg )  # choose method
tk.Radiobutton(window, text = "Metoda bisekcji", variable = method, value = 1, indicator = 0, background = app_bg).pack(side=tk.LEFT, in_=methods, padx=10, pady=10)
tk.Radiobutton(window, text = "Reguła falsi", variable = method, value = 2, indicator = 0, background = app_bg).pack(side=tk.LEFT, in_=methods, padx=10, pady=10)
methods.pack()
epsilon_label = tk.Label(window, bg=app_bg, fg="white", text="Epsilon: ").pack(padx=10, pady=[30, 0])
epsilon = tk.Entry(window, width=30, bg = "#DDDDDD")
epsilon.pack(padx=30)
iterations_label = tk.Label(window, bg=app_bg, fg="white", text="Iterations: ").pack(padx=10, pady=[30, 0])
iterations = tk.Entry(window, width=30, bg = "#DDDDDD")
iterations.pack(padx=30)

boundaries = tk.Frame( window, bg=app_bg )
tk.Label(window, text="Lewa granica:", bg = app_bg, fg="white").pack(side=tk.LEFT, in_=boundaries)
aEntry = tk.Entry(window, width=30, bg = "#DDDDDD")
aEntry.pack(side=tk.LEFT, padx=20, pady=70, in_=boundaries)
tk.Label(window, text="Prawa granica:", bg=app_bg, fg="white").pack(side=tk.LEFT, in_=boundaries)
bEntry = tk.Entry(window, width=30, bg = "#DDDDDD")
bEntry.pack(side=tk.LEFT, padx=20, pady=20, in_=boundaries)
boundaries.pack()

button_compute = tk.Button(window, text="Stwórz wykres", command=click).pack(padx=20, pady=70, side=tk.BOTTOM)

window.mainloop()
