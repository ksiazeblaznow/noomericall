import tkinter as tk
from tkinter import messagebox
import numpy as np
from icecream import ic

window = tk.Tk()
app_bg = '#232329'
window['bg'] = app_bg


# funkcje
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_diagonal(m):
    length = m.shape[0]
    d = 0
    o = 0

    for i in range(length):
        for j in range(length):
            if (i == j):
                d += np.abs(m[i][i])
            else:
                o += np.abs(m[i][j])

    return d >= o

def gauss_seidel(m, n, x):
    l = len(m)

    for j in range(l):
        d = n[j]

        for i in range(l):
            if (j != i):
                d -= m[j][i] * x[i]
        
        x[j] = d / m[j][j]
    

    return x


# funkcje GUI
def load():
    return np.loadtxt("input.txt", dtype='float64', delimiter=',')

def oblicz():
    wynikiX = []
    wynik_var.set('wynik')
    m = load()
    n = np.loadtxt("inputX.txt", dtype='float64', delimiter=',')
    iks = np.zeros(n.shape)

    # sprawdza czy floaty itd.
    if not is_float(epsEntry.get()):
        tk.messagebox.showinfo(title="Halo", message="Epsilon musi być wartością zmiennoprzecinkową (double)")
        return 0
    elif not is_int(iterEntry.get()):
        tk.messagebox.showinfo(title="Halo", message="Liczba iteracji to wartość całkowita")
        return 0

    iters = int(iterEntry.get())
    eps = float(epsEntry.get())
    eps = iters


    # czy zbiezna
    if not (is_diagonal(m)):
        tk.messagebox.showinfo(title="Halo", message="macierz nie jest zbiezna")
        return 0
    else:
        if is_iter.get():
            # iteracyjnie
            for _ in range(iters):
                gauss_seidel(m, n, iks)
            wynik_var.set(iks)
        else:
            # leci epsilonem
            for _ in range(eps):
                gauss_seidel(m, n, iks)
            wynik_var.set(iks)

                
                



    


    # ('\n'.join([' | '.join(['{:6}'.format(item) for item in row])for row in m]))

    ic('policzone', epsEntry.get(), iterEntry.get(), is_iter.get())


def loadMatrix():
    m = load()
    n = np.loadtxt("inputX.txt", dtype='float64', delimiter=',')
    mn = np.vstack((m.T, n)).T  # konkatenacja macierzy here
    matrix.set(('\n'.join([' | '.join(['{:6}'.format(item) for item in row])for row in mn])))


# zmienne
matrix = tk.StringVar()
wynik_var = tk.StringVar()
is_iter = tk.IntVar(0)  # epsilon - 0 | iteracyjnie - 1

# gui
tk.Label(window, bg=app_bg, fg="white",text="Metoda Gaussa-Seidla", font=("Consolas", 30)).pack(padx=100, pady=50)

tk.Button(window, text="Odśwież", command=lambda: [ load(), loadMatrix() ]).pack(side=tk.TOP, padx=20, pady=30)
matrix_display = tk.Label(window, bg=app_bg, fg='white', textvariable=matrix, font=("Consolas", 14))
matrix_display.pack()

loadMatrix()


# matrices2 = tk.Frame( window, bg=app_bg )
# for i in range(0, 5):
#     displayMatrix(matrix, matrices2)
# matrices2.pack()

# iteracja czy epsilon
iter_eps = tk.Frame(window, bg=app_bg)
tk.Radiobutton(iter_eps, bg=app_bg, fg="orange", text="EPSILON", value = 0, indicator = 0, variable=is_iter).pack(side=tk.LEFT, in_=iter_eps, padx=40, pady=40)
tk.Radiobutton(iter_eps, bg=app_bg, fg="orange", text="ITERACYJNIE", value = 1, indicator = 0, variable=is_iter).pack(side=tk.LEFT, in_=iter_eps ,padx=40, pady=40)
iter_eps.pack()

iter_eps2 = tk.Frame(window, bg=app_bg)
tk.Label(window, text="Epsilon:", bg = app_bg, fg="white", font=("Consolas", 14)).pack(side=tk.LEFT, in_=iter_eps2)
epsEntry = tk.Entry(iter_eps2, width=30, bg = "#DDDDDD")
epsEntry.pack(side=tk.LEFT, padx=20, pady=70, in_=iter_eps2)
tk.Label(window, text="Iteracji:", bg = app_bg, fg="white", font=("Consolas", 14)).pack(side=tk.LEFT, in_=iter_eps2)
iterEntry = tk.Entry(iter_eps2, width=30, bg = "#DDDDDD", text='xd')
iterEntry.pack(side=tk.LEFT, padx=20, pady=70, in_=iter_eps2)
iter_eps2.pack()

# guzik liczenia
tk.Button(window, padx=60, pady=10, font=20, bg="#171717", bd=10, text='Oblicz', fg="#CCFFEE", command=oblicz).pack(pady='50')

# wyswietl wynik
wynik = tk.Label(window, bg=app_bg, fg='white', textvariable=wynik_var, font=("Consolas", 14))
wynik.pack(pady=[0, 100])

window.mainloop()
