def main():
  graph = {0: {1, 2, 3}, 1: {0}, 2: {0}, 3: {4, 5}, 4: {3}, 5: {3}}
  visited = []
  v = 0
  T = []
  T.append(v)
  visited.append(v)
  while len(T):
    u = T.pop()
    print(u + 1)
    for w in graph[u]:
      if w not in visited:
        T.append(w)
        visited.append(w)

if __name__ == '__main__':
  main()