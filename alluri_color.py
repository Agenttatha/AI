from constraint import Problem, AllDifferentConstraint

def graph_coloring(colors_dict, vertices, paths):
    problem = Problem()

    # Add variables for each vertex
    for vertex in vertices:
        problem.addVariable(vertex, list(colors_dict.keys()))  # Use color names as domain

    # Add constraints for adjacent vertices
    for path in paths:
        v1, v2 = path
        problem.addConstraint(AllDifferentConstraint(), (v1, v2))  # Ensure adjacent vertices have different colors

    # Solve the problem
    solution = problem.getSolution()
    if solution is None:
        print("No solution found.")
        return

    # Print the solution
    print("Vertex assignments:")
    for vertex, color in solution.items():
        print(f"{vertex}: Color {color}")

# Example usage
colors_dict = {"Red": 1, "Green": 2, "Blue": 3}  # Example colors dictionary
vertices = ['A', 'B', 'C', 'D']  # Example vertices
paths = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]  # Example paths
graph_coloring(colors_dict, vertices, paths)
