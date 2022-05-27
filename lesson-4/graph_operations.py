graph1 = {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}}
graph2 = {2: {3, 4}, 3: {2}, 4: {2}}
merged = graph2
for key, value in graph1.items():
    if key not in merged:
        merged[key] = value
    else:
        merged[key].update(value)
print('***Объединение***')
print(merged)


graph1 = {1: {2, 3}, 2: {1}, 3: {1}}
graph2 = {4: {5}, 5: {4, 6}, 6: {5}}
merged = graph1.copy()
merged[1].update({4})
for i in graph2:
    for key, item in merged.items():
        merged[key].update({i})
merged.update(graph2)
for i in graph1:
    for j in graph2:
        merged[j].update({i})
print('***Соединение***')
print(merged)


graph1 = {1: {2, 3, 4}, 2: {1,3}, 3: {1, 2}, 4: {1}}
graph2 = {2: {3, 4}, 3: {2}, 4: {2}}
ans = {}
for key, value in graph1.items():
    if key in graph2:
        a = set()
        for i in graph1[key]:
            if i in graph2[key]:
                a.update({i})
        if len(a) == 0:
            ans.update({key: {}})
        else:
            ans.update({key: a})
print('***Пересечение***')
print(ans)


graph1 = {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}}
vertices =[]
for i in graph1:
    vertices.append(i)
for key, value in graph1.items():
    new_key = set()
    for j in vertices:
        if j not in graph1[key] and j != key:
            new_key.update({j})
    graph1[key] = new_key
    if len(graph1[key])  == 0:
        graph1[key] = {}
print('***Дополнение***')
print(graph1)


graph1 = {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}}
vertice_to_delete = 4
edges_to_delete = graph1[vertice_to_delete]
for key, value in graph1.items():
    graph1[key].discard(vertice_to_delete)
del graph1[vertice_to_delete]
print('***Удаление***')
print(graph1)