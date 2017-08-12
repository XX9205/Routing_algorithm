# -*- coding: utf-8 -*-
# conding=utf-8
import networkx as nx

if __name__ == '__main__':
    graph = nx.DiGraph()
    link_list = {(0,1):10,(0,4):5,(4,1):3,(1,4):2,(1,2):1,(2,3):4,(3,2):6,(3,0):7,(4,3):2,(4,2):9}

    for src in range(5):
        for dst in range(5):
            graph.add_edge(src, dst, weight=float('inf'))
            if src == dst:
                graph.add_edge(src, dst, weight=0)
            elif (src, dst) in link_list.keys():
                graph.add_edge(src, dst, weight=link_list[(src, dst)])

    #path = nx.all_simple_paths(graph, source=0, target=3, cutoff=5)
    #k_path = nx.shortest_simple_paths(graph, source=0, target=4)
    path_generator = nx.shortest_simple_paths(graph, source=0,
                                              target=3, weight='weight')
    print(list(path_generator))
    #print 'NetwokX:', '\n'
    #print graph, "not output graph", '\n'
    #print list(path), '\n'
    #print list(k_path), '\n'
    #print graph.get_edge_data(2, 1)

    jiance = []
    sp = [2, 5, 6, 8, 9]
    lenth = len(sp)
    for i in range(lenth-1):
        jiance.append((sp[i], sp[i+1]))
    #print jiance

    a = {(2,3):[2,1]}
    #print a
    a[(2,3)] = [2,3,5]
    #print a
