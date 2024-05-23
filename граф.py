import matplotlib.pyplot as plt
import networkx as nx
import numpy as np 

def find_max_independent_set(graph, current_set, current_vertex):
  global max_independent_set
  if current_vertex == len(graph):  #ужэе к крнцу  графа
    if len(current_set) > len(max_independent_set):
      max_independent_set = set(current_set)
    return

  # Тут типо проверочка является ли текущая вершина независимой
  is_independent = True
  for vertex in current_set:
    if graph[current_vertex][vertex] == 1:
      is_independent = False
      break

  if is_independent:
    #  вершину в множество
    new_set = set(current_set)
    new_set.add(current_vertex)
    find_max_independent_set(graph, new_set, current_vertex + 1)
  find_max_independent_set(graph, current_set, current_vertex + 1)

# матрица смежности
#graph = [[0, 1, 0, 1, 1, 0, 0],
 #        [1, 0, 1, 0, 1, 1, 0],
     #    [0, 1, 0, 0, 0, 1, 0],
     #    [1, 0, 0, 0, 0, 0, 0],
     #    [1, 1, 0, 0, 0, 1, 0],
      #   [0, 1, 1, 0, 1, 0, 1],
      #   [0, 0, 0, 0, 0, 1, 0],]


graph = [[0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,1],
         [0,1,1,0,0],
         [0,0,1,0,0]]

H=[]
#Nlines = input('Raws num: ')
#for k in range(Nlines):
    #graph.append(H=input('line - ', k,': '))

max_independent_set = set()
find_max_independent_set(graph, set(), 0)

# в визульн. граф =0
G = nx.from_numpy_array(np.array(graph))

plt.figure(figsize=(10, 6))  

# Создаем подграфики
plt.subplot(1, 2, 1)  # 1 2, 3  первый подграфик
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500)
plt.title("Граф")

plt.subplot(1, 2, 2)  # 1 2 3 второй подграфик
plt.text(0.5, 0.5, f"Наибольшее независимое множество: {max_independent_set}\n\n"
              f"Матрица смежности:\n\n"
              f"{np.array(graph)}",
         ha='center', va='center', fontsize=12)
plt.axis('off')

plt.tight_layout()  # Подгоняем подграфики
plt.show()