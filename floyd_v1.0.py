# -*- coding: utf-8 -*-
# conding=utf-8
import copy
def floyd(graph):
    path = {}
    list = copy.deepcopy(graph)
    length = len(list)

    for i in range(length):
        path.setdefault(i, {})
        for j in range(length):
            path[i].setdefault(j, -1)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if (list[i][k] < ini and list[k][j] < ini and list[i][j] > list[i][k] + list[k][j]):
                    list[i][j] = list[i][k] + list[k][j]
                    path[i][j] = k
    return list, path

def output(a, b):
    if a == b:
        out_path.append(b)
    if path[a][b] == -1:
        out_path.append(b)
    else:
        output(a, path[a][b])
        output(path[a][b], b)


if __name__ == '__main__':
    ini = float('inf')
    graph_list = [[0, 10, ini, ini, 5], [ini, 0, 1, ini, 2], [ini, ini, 0, 4, ini], [7, ini, 6, 0, ini],
                    [ini, 3, 9, 2, 0]]
    out_path = []
    new_graph, path = floyd(graph_list)

    out_path.append(2)
    output(2, 1)
    
    print(graph_list)
    print('\n\n', path)
    print('\n\n', new_graph)
    print('\n\n', out_path)
