
def main():
  # C = [
  #     [-1, 10, 30, 50, 10],
  #     [-1, -1, -1, -1, -1],
  #     [-1, -1, -1, -1, 10],
  #     [-1, 40, 20, -1, -1],
  #     [10, -1, 10, 30, -1]
  # ]
  C = [
      [-1, 5, 10, -1, -1],
      [-1, -1, -1, 15, -1],
      [-1, -1, -1, 5, -1],
      [-1, 15, -1, -1, 10],
      [-1, 15, -1, -1, -1]
  ]
  inf = 1000
  start = 0
  values = [0, inf, inf, inf, inf]
  visited = []
  current_vertex = start
  last_vertex_path = [start for i in range(len(C))]
  while len(visited) < len(C):
    neighbours = [i for i in range(len(C)) if C[current_vertex][i] != -1]
    for neighbour in neighbours:
      if values[current_vertex] + C[current_vertex][neighbour] <= values[neighbour]:
        values[neighbour] = values[current_vertex] + \
            C[current_vertex][neighbour]
        last_vertex_path[neighbour] = current_vertex
    visited.append(current_vertex)
    unvisited = [i for i in range(len(C)) if not i in visited]
    unvisited_values = [values[i] for i in unvisited]
    if unvisited_values:
      current_vertex = unvisited[unvisited_values.index(min(unvisited_values))]
  paths = [[] for _ in range(len(C))]
  for i in range(len(C)):
    current_path_vertex = last_vertex_path[i]
    paths[i].append(current_path_vertex)
    while current_path_vertex != start:
      current_path_vertex = last_vertex_path[paths[i][-1]]
      paths[i].append(current_path_vertex)
    paths[i] = list(reversed(paths[i]))
    paths[i].append(i)
  for i in range(len(last_vertex_path)):
    if i != start:
      print(
          f'Path to {i + 1} is {[j + 1 for j in paths[i]]} with value {values[i]}')


if __name__ == '__main__':
  main()
