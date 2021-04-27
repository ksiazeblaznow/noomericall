from matplotlib import pyplot as plt
import numpy as np
import calculations


def get_fun():
    in_number = ''
    while in_number not in list(map(str, range(1, 5))):
        in_number = input('Prosze wybrac wzor funkcji \n'
                          '1. 2 * x - 9 \n'
                          '2. 3 * x ** 3 - 5 \n'
                          '3. np.sin(x ** 2) - np.cos(x)  \n'
                          '4. 5*np.absolute(np.sin(x)-2) \n'
                          '')
    return in_number


def get_range():
    print('Poczatek przedzialu:')
    a = input()
    print('Koniec przedzialu')
    b = input()
    return float(a), float(b)


def get_nodes_number():
    return int(input('Liczba wezlow: \n'))


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
            print('Nieprawidlowe dane w pliku. Trwa losowanie')
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


def nodes_choice():
    choice = ''
    while choice != '1' and choice != '2':
        choice = input("Wezly: \n 1. Losowanie polozenie wezlow \n "
                       "2. Wczytaj polozenie wezlow z pliku nodes.txt \n")
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


def get_all_graphs(formula_range, formula, nodes, nodes_values, newton):
    get_function_graph(formula_range, formula)
    plt.plot(newton[0], newton[1], '*', zorder=0, linewidth=4,
             label='Wykres wielomianu interpolacyjnego metody Newtona')
    plt.scatter(nodes, np.array(nodes_values), label='Węzły interpolacyjne')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    plt.savefig('wykres.png',
                dpi=300,
                format='png',
                bbox_inches='tight')
    plt.show()

