import in_output
import calculations


*data, nodes = in_output.menu()

nodes_values = calculations.get_nodes_values(nodes, data[1])

newton = calculations.get_all_results(data[0], nodes_values, nodes, calculations.newton_interpolation)

in_output.get_all_graphs(data[0], data[1], nodes, nodes_values, newton)
