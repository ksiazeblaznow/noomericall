import tkinter as tk
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

    return d > o

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

def displayMatrix(m, frame):
    tk.Label(window, bg=app_bg, fg="white", text="matrix1:")
    tk.Label(frame, bg=app_bg, fg="white",text=('\n'.join([' | '.join(['{:6}'.format(item) for item in row])
        for row in matrix])), font=("Consolas", 9)).pack(side=tk.LEFT, in_=frame, padx='30', pady='30')

def oblicz():
    print('liczymy')
    if dupa.winfo_ismapped():
        dupa.pack_forget()
    else:
        dupa.pack()

# zmienne
matrix = load()
print(matrix)
is_iter = tk.IntVar(0)
iters = tk.IntVar()
epsilon = float()

# gui
tk.Label(window, bg=app_bg, fg="white",text="Metoda Gaussa-Seidla", font=("Consolas", 30)).pack(padx=100, pady=50)

matrices = tk.Frame( window, bg=app_bg )
for i in range(0, 5):
    displayMatrix(matrix, matrices)
matrices.pack()

matrices2 = tk.Frame( window, bg=app_bg )
for i in range(0, 5):
    displayMatrix(matrix, matrices2)
matrices2.pack()

# iteracja czy epsilon
iter_eps = tk.Frame(window, bg=app_bg)
tk.Radiobutton(iter_eps, bg=app_bg, fg="orange", text="ITERACYJNIE", value = 0, indicator = 0, variable=is_iter).pack(side=tk.LEFT, in_=iter_eps ,padx=40, pady=40)
tk.Radiobutton(iter_eps, bg=app_bg, fg="orange", text="EPSILON", value = 1, indicator = 0, variable=is_iter).pack(side=tk.LEFT, in_=iter_eps, padx=40, pady=40)
iter_eps.pack()

# guzik liczenia
tk.Button(window, padx=60, pady=10, font=20, bg="#171717", bd=10, text='jazda', fg="white", command=oblicz).pack(pady='50')

dupa = tk.Label(window, text="DUPA")
dupa.pack()

window.mainloop()
