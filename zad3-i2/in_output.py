from matplotlib import pyplot as plt
import numpy as np
import calculations
import sys


def get_fun():
    in_number = ''
    while in_number not in list(map(str, range(1, 5))):
        in_number = input('Prosze wybrac wzor funkcji \n '
                          '1. 2 * x - 9 \n'
                          '2. 3 * x ** 3 - 5 \n'
                          '3. np.sin(x ** 2) - np.cos(x)  \n'
                          '4. 5*np.absolute(np.sin(x)-2) \n'
                          '')
    return in_number


def get_range():
    print('Prosze podac poczatek przedzialu')
    a = input()
    print('Prosze podac koniec przedzialu')
    b = input()
    return float(a), float(b)


def get_nodes_number():
    return int(input('Prosze podac liczbe wezlow \n'))


def get_unknowns(unknowns_number, formula_range):
    unknowns = []
    for i in range(unknowns_number):
        users_in = input('Prosze podac wartosc wspolrzednej x punktu do obliczenia wartosci'
                         ' jego wspolrzednej y za pomoca obu metod interpolacji ')
        while not (users_in.isdigit()) and not (formula_range[1] >= float(users_in) >= formula_range[0]):
            print('Prosze podac prawidlowa wartosc')
            users_in = input()
        unknowns.append(float(users_in))
    return np.array(unknowns)


def get_unknowns_number():
    number = ''
    while not number.isdigit():
        number = input('Prosze podac liczbe poszukiwanych niewiadomych wartosci wielomianu dla danych x \n')
    return int(number)


def menu():
    formula = get_fun()
    formula_range = get_range()
    choice = nodes_choice()
    if choice == '1':
        nodes_number = get_nodes_number()
        nodes = get_nodes_user(nodes_number, formula_range)
    else:
        nodes = get_nodes_file(formula_range)
        if not nodes:
            print('Dane w pliku sa nieprawidlowe, zostana wylosowane')
            nodes_number = get_nodes_number()
            nodes = get_nodes_user(nodes_number, formula_range)
    checked_formula = formula_switcher(formula)
    return [formula_range, checked_formula, nodes]


def formula_switcher(in_number):
    switcher = {
        '1': '2 * x - 9',
        '2': '3 * x ** 3 - 5',
        '3': 'np.sin(x ** 2) - np.cos(x)',
        '4': '5*np.absolute(np.sin(x)-2)'
    }
    return switcher.get(in_number, 'invalid input')


def unknowns_menu(formula_range):
    unknowns_number = get_unknowns_number()
    return get_unknowns(unknowns_number, formula_range)


def nodes_choice():
    choice = ''
    while choice != '1' and choice != '2':
        choice = input("Prosze wybrac: \n 1. Polozenia wezlow maja zostac wylosowane \n "
                       "2. Poloznia wezlow maja zostac wczytane z pliku 'nodes.txt' \n")
    return choice


def get_nodes_file(formula_range):
    nodes = np.genfromtxt(fname='nodes.txt', delimiter=",")

    return validate_nodes_file(formula_range, nodes)


def get_nodes_user(nodes_number, formula_range):  # pobiera liczbę węzłów i sposób ich wybrania
    nodes = np.random.uniform(low=formula_range[0], high=formula_range[1], size=nodes_number)
    nodes = np.sort(nodes)
    return np.array(nodes)


def validate_nodes_file(formula_range, nodes):  # sprawdza, czy dane w nodes.txt są prawidłowe
    valid_nodes = [element for element in nodes if formula_range[0] <= element < formula_range[1]]
    return valid_nodes


def get_function_graph(formula_range, formula):
    x = np.linspace(formula_range[0], formula_range[1])
    y = []
    for i in range(len(x)):
        y.append(calculations.get_fun_value(formula, x[i]))
    plt.plot(x, np.array(y), label='Wykres funkcji')


def get_all_graphs(formula_range, formula, nodes, nodes_values, lagrange, newton):
    get_function_graph(formula_range, formula)
    plt.plot(lagrange[0], lagrange[1], '--', zorder=0, linewidth=4,
             label='Wykres wielomianu interpolacyjnego metody Lagrange')
    plt.plot(newton[0], newton[1], '*', zorder=0, linewidth=4,
             label='Wykres wielomianu interpolacyjnego metody Newtona')
    plt.scatter(nodes, np.array(nodes_values), label='Węzły interpolacyjne')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.savefig('wykres.png',
                dpi=300,
                format='png',
                bbox_inches='tight')
    plt.show()


def data_output(unknowns, nodes, formula, nodes_values):
    print('Punkty podane przez użytkownika do obliczenoia dwoma metodami \n', unknowns)
    # lagrange = []
    newton = []
    true_values = []
    for x in unknowns:
        # lagrange.append(calculations.lagrange_interpolation(x, nodes, nodes_values))
        newton.append(calculations.newton_interpolation(x, nodes, nodes_values))
        true_values.append(calculations.get_fun_value(formula, x))
    true_values = np.array(true_values)
    # lagrange = np.array(lagrange)
    newton = np.array(newton)
    # lagrange_errors = calculations.get_residuals(true_values, lagrange)
    newton_errors = calculations.get_residuals(true_values, newton)
    # lagrange_sq_error = calculations.get_mse(lagrange_errors)
    newton_sq_error = calculations.get_mse(newton_errors)
    print('Prawidlowe wartosci dla danych niewiadomych \n', true_values)
    # print('Wyniki metody lagrange \n', lagrange)
    print('Wyniki metody Newtona \n', newton)
    # print('Bledy metody lagrange \n', lagrange_errors)
    print('Bledy metody Newtona \n', newton_errors)
    # print('Sredni blad kwadratowy metody lagrange \n', lagrange_sq_error)
    print('Sredni blad kwadratowy metody Newtona \n', newton_sq_error)
