import operator
from collections import OrderedDict
from typing import List, Any, Dict

import igraph

from Graphs.EdgeType import EdgeType
from Graphs.Graph import Graph
import Vertex
import Edge
import sys
from Lab02.Queue import Queue


def paths_count(g: Graph, a: Any, b: Any) -> int:
    lst: List[Vertex] = g.list_of_v
    found_a = None
    found_b = None
    for i in lst:
        if i.data == a:
            found_a = i
        if i.data == b:
            found_b = i

    if found_a is None:
        raise ValueError("Vertex A was not found")
    if found_b is None:
        raise ValueError("Vertex B was not found")

    result = g.find(found_a, found_b)
    return len(result)


class GraphPath:
    __begin: Vertex
    __end: Vertex
    weighted: bool
    g: Graph
    pth: list[Edge]

    def dijkstra_algorithm(self):
        visited: list[Vertex] = [self.__begin]
        cost: Dict[Vertex, float] = {}
        for i in self.g.adjacencies.keys():
            cost[i] = sys.float_info.max
        cost[self.__begin] = 0.

        q: Queue = Queue()
        cnE: list[Edge] = []
        unvisited_nodes: list[list[Vertex, float]] = []
        current_node: list[Vertex] = []
        paths: Dict[Vertex, list[Edge]] = {}
        for i in self.g.adjacencies.keys():
            paths[i] = []

        for i in self.g.adjacencies[self.__begin]:
            cnE.append(i)
            current_node.append(i.destination)

        result: list[Edge] = []
        found: bool = False
        while len(cnE) != 0 or len(unvisited_nodes) != 0:
            lowest: float = sys.float_info.max
            lowest_node: Vertex = None

            # if node has no neighbours
            if len(cnE) == 0:
                if len(unvisited_nodes) != 0:
                    srt = sorted(unvisited_nodes, key=operator.itemgetter(1))
                    unvisited_nodes = srt
                    node = unvisited_nodes.pop()
                    ver: Vertex = node[0]
                    for i in self.g.adjacencies:
                        if i == ver:
                            for ne in self.g.adjacencies[ver]:
                                cnE.append(ne)
                                current_node.append(ne.destination)
                else:
                    return result

            # current node checker
            for e in cnE:
                if e.destination == self.__end:
                    found = True
                weight: float = e.weight + cost[e.source]
                if cost[e.destination] > weight:
                    cost[e.destination] = weight
                    visited.append(e.destination)
                    paths[e.destination] = paths[e.source].copy()
                    paths[e.destination].append(e)
                if weight < lowest:
                    lowest = weight
                    lowest_node = e.destination

            # check if any path to current node is present
            for e in cnE:
                to_check: list[Edge] = self.g.adjacencies[e.destination]

                for neighbour in to_check:
                    if neighbour.destination in current_node or visited:
                        weight: float = neighbour.weight + cost[e.source]
                        if cost[neighbour.destination] > weight:
                            paths[neighbour.destination] = paths[neighbour.source].copy()
                            paths[neighbour.destination].append(neighbour)
                            if weight < lowest:
                                lowest = weight
                                lowest_node = e.destination

            for v in current_node:
                visited.append(v)

            copy_of_cn: list[Vertex] = current_node.copy()
            current_node = []
            cnE = []
            for v in copy_of_cn:
                for i in self.g.adjacencies[v]:
                    wgh = cost[i.source] + i.weight
                    if i.destination not in visited and (not found or wgh < cost[self.__end]):
                        unvisited_nodes.append([[i.destination], cost[i.source] + i.weight])

            if lowest_node is not None:
                for next_e in self.g.adjacencies[lowest_node]:
                    cnE.append(next_e)
                    current_node.append(next_e.destination)

        if found:
            return paths[self.__end]

    def find(self):
        if self.weighted:
            self.pth = self.dijkstra_algorithm()
        else:
            self.pth = self.search_unweighted()

    def show(self):

        if self.pth is None:
            print("No path yet")
            return

        is_directed: bool = False

        if self.g.type_of_g == EdgeType.directed:
            is_directed = True

        g: igraph.Graph = igraph.Graph(directed=True)
        for i in self.g.list_of_v:
            g.add_vertex(str(i.index))

        def ae(v: Vertex):
            for i in self.g.adjacencies[v]:
                g.add_edge(str(v.index), str(i.destination.index))
                tmp = g.get_eid(str(v.index), str(i.destination.index))
                es = igraph.EdgeSeq(g)
                es[tmp]["weight"] = i.weight
                es[tmp]["label"] = str(i.weight)

        for i in self.g.list_of_v:
            ae(i)

        for edge in g.es:
            edge["label"] = edge["weight"]

        for i in self.pth:
            es = igraph.EdgeSeq(g)
            tmp = g.get_eid(str(i.source.index), str(i.destination.index))
            es[tmp]["color"] = "blue"

        g.vs["label"] = g.vs["name"]
        g.vs["label_color"] = "black"
        g.vs["size"] = 20
        g.vs["color"] = "white"

        igraph.plot(g)
        return

    def search_unweighted(self) -> list[Edge]:
        visited: list[[Vertex]] = [[self.__begin]]
        visited_edge: list[[Edge]] = []
        cp: list[Edge] = []
        q: Queue = Queue()
        q.enqueue([self.__begin])
        while len(q) != 0:
            p: list[Vertex] = q.dequeue()
            v: Vertex = p[-1]
            for n in self.g.adjacencies[v]:
                if n.destination not in p:
                    np: list[Vertex] = p.copy()
                    np.append(n.destination)
                    if n.destination == self.__end:
                        result: list[Edge] = []
                        for i in range(0, len(np) - 1):
                            e: Edge
                            for j in self.g.adjacencies[np[i]]:
                                if j.destination == np[i + 1]:
                                    e = j
                                    result.append(e)
                        return result
                    q.enqueue(np)
        return []

    def __init__(self, graph: Graph, begin: Vertex, end: Vertex):
        self.__begin = begin
        self.__end = end
        self.g = graph
        self.weighted = False
        self.path = []
        self.pth = None

        for i in graph.adjacencies:
            for j in graph.adjacencies[i]:
                if j.weight is not None:
                    self.weighted = True
                    return


G: Graph = Graph()
for i in range(0, 6):
    G.create_vertex("v" + str(i))

G.add_directed_edge(G.list_of_v[0], G.list_of_v[1])
G.add_directed_edge(G.list_of_v[0], G.list_of_v[5])
G.add_directed_edge(G.list_of_v[5], G.list_of_v[2])
G.add_directed_edge(G.list_of_v[5], G.list_of_v[1])
G.add_directed_edge(G.list_of_v[4], G.list_of_v[5])
G.add_directed_edge(G.list_of_v[4], G.list_of_v[1])
G.add_directed_edge(G.list_of_v[2], G.list_of_v[1])
G.add_directed_edge(G.list_of_v[2], G.list_of_v[3])
G.add_directed_edge(G.list_of_v[3], G.list_of_v[4])
G.add_directed_edge(G.list_of_v[3], G.list_of_v[4])
G.add_directed_edge(G.list_of_v[3], G.list_of_v[3])

G_disconnected: Graph = Graph()

for i in range(0, 11):
    G_disconnected.create_vertex(str(i))

idk_what_else_I_can_do: Graph = Graph()
for i in range(0, 6):
    idk_what_else_I_can_do.create_vertex(i)

idk_what_else_I_can_do.add_undirected_edge(idk_what_else_I_can_do.list_of_v[3], idk_what_else_I_can_do.list_of_v[4])
idk_what_else_I_can_do.add_directed_edge(idk_what_else_I_can_do.list_of_v[1], idk_what_else_I_can_do.list_of_v[5])
idk_what_else_I_can_do.add_directed_edge(idk_what_else_I_can_do.list_of_v[0], idk_what_else_I_can_do.list_of_v[3])
idk_what_else_I_can_do.add_directed_edge(idk_what_else_I_can_do.list_of_v[2], idk_what_else_I_can_do.list_of_v[1])

# normal path
print(paths_count(G, "v0", "v1"))
# loop
print(paths_count(G, "v3", "v3"))
# self reference with no loop
print(paths_count(idk_what_else_I_can_do, 4, 4))
# no connections
print(paths_count(G_disconnected, "0", "10"))
# empty is forbidden bcs i cannot pass vertices by value if there are no vertices

# different no connections
print(paths_count(idk_what_else_I_can_do, 3, 1))
# separated graph
print(paths_count(idk_what_else_I_can_do, 0, 4))
print(paths_count(idk_what_else_I_can_do, 2, 5))

# G_disconnected.show()
# idk_what_else_I_can_do.show()
# G.show()

# ls = G.find(G.list_of_v[5], G.list_of_v[1])
#
# iter = 1
# for i in ls:
#     print("\n" + str(iter) +".")
#     for j in i:
#         print(j)
#     iter += 1


# Dijkstra
G2: Graph = Graph()

for i in range(0, 4):
    G2.create_vertex("v" + str(i))

G2.add(EdgeType.directed, G2.list_of_v[0], G2.list_of_v[1], 30)
G2.add(EdgeType.directed, G2.list_of_v[1], G2.list_of_v[3], 2)
G2.add(EdgeType.directed, G2.list_of_v[0], G2.list_of_v[2], 10)
G2.add(EdgeType.directed, G2.list_of_v[2], G2.list_of_v[1], 5)
G2.add(EdgeType.directed, G2.list_of_v[2], G2.list_of_v[3], 9)

dij: GraphPath = GraphPath(G2, G2.list_of_v[0], G2.list_of_v[3])

dij.find()
dij.show()
dij_list = dij.dijkstra_algorithm()
for i in dij_list:
    print(i)
