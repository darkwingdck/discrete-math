def main(v, graph):
  visited = []
  T = []
  comp = []
  T.append(v)
  visited.append(v)
  while len(T):
    u = T.pop()
    comp.append(u)
    for w in graph[u]:
      if w not in visited:
        T.append(w)
        visited.append(w)
  return comp

if __name__ == '__main__':
  graph = {0: {1, 2, 3}, 1: {0}, 2: {0}, 3: {4, 5}, 4: {3}, 5: {3}, 6: {7}, 7: {6}}
  v = 0
  visited = []
  ans = []
  while v < len(graph):
    if v not in visited:
      q = main(v, graph)
      visited.extend(q)
      ans.append(q)
      v = v + 1
    else:
      v = v + 1

  print(ans)