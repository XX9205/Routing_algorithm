# -*- coding: utf-8 -*-
# conding=utf-8
def floyd(graph):
    length = len(graph)
    path = {}
    # mypath = {}
    for k in range(length):
        for i in range(length):
            path.setdefault(i, {})
            for j in range(length):
                path[i].setdefault(j, [i, j])
                path[i].setdefault(k, [i, k])
                path[k].setdefault(j, [k, j])
                new_node = None

                new_len = graph[i][k] + graph[k][j]
                if graph[i][j] > new_len:
                    graph[i][j] = new_len
                    new_node = k
                if new_node == k:
                    path[i][j] = path[i][k] + path[k][j][1:]

    return graph, path


if __name__ == '__main__':
    ini = float('inf')
    graph_list = [[0, 10, ini, ini, 5],
                  [ini, 0, 1, ini, 2],
                  [ini, ini, 0, 4, ini],
                  [7, ini, 6, 0, ini],
                  [ini, 3, 9, 2, 0],]

    new_graph, path = floyd(graph_list)
    traffic_path = path[2][1]
    print(new_graph)
    print('\n\n', path)
    print('\n\n', traffic_path)
