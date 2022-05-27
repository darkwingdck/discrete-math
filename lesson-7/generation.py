
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random


def main2():
  def ER(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
      a = random()
      if a < p:
        E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g

  n = 4
  p = 0.5
  G = ER(n, p)
  pos = nx.spring_layout(G)
  nx.draw_networkx(G, pos)
  plt.title("Random Graph Generation")
  plt.show()


def upd(graph: dict):
  for vertex in graph:
    for neighbour in graph[vertex]:
      if not vertex in graph[neighbour]:
        graph[neighbour].append(vertex)
  return graph


def main():
  n = 4
  m = 3
  graph = {i: [] for i in range(n)}
  unused = [i for i in range(n)]
  count = 0
  used = []
  for vertex in range(n):
    vertexes = [i for i in range(len(graph)) if i != vertex and i not in used]
    for i in range(n - 1):

      graph[vertex].append(vertexes.pop(0))
      count += 1
      if count == m:
        break
    used.append(vertex)
    if count == m:
      break
  upd(graph)
  print(graph)


if __name__ == '__main__':
  # Если плотность это 2 * кол-во ребер / кол-во вершин * (кол-во вершин - 1)
  main()
  # Если плотность это вероятность того, что ребро существует между заданной парой узлов
  # mian2()
