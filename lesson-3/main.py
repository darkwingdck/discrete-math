graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1', '4']),
         '4': set(['1', '3'])}


def adjacency_matrix(graph: dict):
  keys = list(graph.keys())
  adjacency_matrix = [['-', *(i for i in keys)]]
  for i in range(1, len(graph) + 1):
    adjacency_matrix.append([])
    adjacency_matrix[i].append(keys[i - 1])
    for j in keys:
      if j == keys[i - 1]:
        adjacency_matrix[i].append('-')
      else:
        adjacency_matrix[i].append(1 if j in graph[keys[i - 1]] else 0)
  return adjacency_matrix


def main():
  # Input graph
  graph = {}
  print('Enter a number of vertexes in graph: ')
  vertex_count = int(input())
  for i in range(vertex_count):
    print(f'Neighbours of {i} vertex: ', end="")
    neighbours = map(int, input().split())
    graph[i] = set(neighbours)
  print('Your graph: ', graph)
  # Adjacency matrix
  adjacency_matrix_graph = adjacency_matrix(graph)
  for i in range(len(adjacency_matrix_graph)):
    print(*adjacency_matrix_graph[i])
  # Subgraph vertex input
  print('Enter the set of edges to cut out: ', end="")
  required_edges = list(map(int, input().split()))
  not_required_edges = set(adjacency_matrix_graph[0]) - set(required_edges)
  subgraph = {}
  for i in required_edges:
    subgraph[i] = graph[i]
  for vertex in subgraph:
    for i in not_required_edges:
      if i in subgraph[vertex]:
        subgraph[vertex].remove(i)
  print('Subgraph', subgraph)
  adjacency_matrix_subgraph = adjacency_matrix(subgraph)
  for i in range(len(adjacency_matrix_subgraph)):
    print(*adjacency_matrix_subgraph[i])


if __name__ == "__main__":
  main()
