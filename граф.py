import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def find_max_independent_sets(graph):
    max_independent_sets = []
    max_size = 0

    def dfs(current_set, current_vertex):
        nonlocal max_independent_sets, max_size
        if current_vertex == len(graph):
            if len(current_set) > max_size:
                max_size = len(current_set)
                max_independent_sets = [set(current_set)]
            elif len(current_set) == max_size:
                max_independent_sets.append(set(current_set))
            return

        is_independent = True
        for vertex in current_set:
            if graph[vertex][current_vertex] == 1 or graph[current_vertex][vertex] == 1:
                is_independent = False
                break

        if is_independent:
            new_set = set(current_set)
            new_set.add(current_vertex)
            dfs(new_set, current_vertex + 1)
        dfs(current_set, current_vertex + 1)

    dfs(set(), 0)
    return max_independent_sets


matrix = []

def write_digits_to_array():
    user_input = input("Введи строку: ")
    digits_array = []
    
    for digit in user_input:
        if digit.isdigit():
            digits_array.append(int(digit))
    
    print("Digits array:", digits_array)
    return digits_array

o = input("Введите размерность матрицы смежности: ")
for i in range(int(o)): 
  matrix.append(write_digits_to_array())

print(matrix)

graph = [[int(digit) for digit in user_input] for user_input in matrix]





max_independent_sets = find_max_independent_sets(graph)

G = nx.from_numpy_array(np.array(graph))

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500)
plt.title("Graph")

plt.subplot(1, 2, 2)
text = "Max independent sets:\n\n"
for i, max_set in enumerate(max_independent_sets):
    text += f"Set {i+1}: {max_set}\n"
text += f"\nМатрица смежности:\n\n{np.array(graph)}"

plt.text(0.5, 0.5, text, ha='center', va='center', fontsize=12)
plt.axis('off')

plt.tight_layout()
plt.show()