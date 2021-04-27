import in_output
import calculations
data = in_output.menu()
nodes = data[2]
nodes_values = calculations.get_nodes_values(nodes, data[1])
lagrange = calculations.get_all_results(data[0], nodes_values, nodes, calculations.lagrange_interpolation)
newton = calculations.get_all_results(data[0], nodes_values, nodes, calculations.newton_interpolation)
in_output.get_all_graphs(data[0], data[1], nodes, nodes_values, lagrange, newton)
unknowns = in_output.unknowns_menu(data[0])
in_output.data_output(unknowns, nodes, data[1], nodes_values)
lagrange = calculations.lagrange_interpolation(5, nodes, nodes_values)
newton2 = calculations.newton_interpolation(5, nodes, nodes_values)
