from typing import Dict, List, Any, Optional, Callable
import igraph
from igraph import plot
from Vertex import Vertex
from Edge import Edge
from EdgeType import EdgeType
from Lab02.Queue import Queue


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
    list_of_v: List[Vertex]
    type_of_g: EdgeType
    idx: int

    def create_vertex(self, data: Any) -> Vertex:
        vertex: Vertex = Vertex(data)
        vertex.index = self.idx
        self.idx += 1
        self.adjacencies[vertex] = []
        self.list_of_v.append(vertex)
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        assert source in self.list_of_v
        assert destination in self.list_of_v
        if self.type_of_g == EdgeType.undirected:
            self.type_of_g = EdgeType.directed
        edge: Edge = Edge(source, destination, EdgeType.directed, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        assert source in self.list_of_v
        assert destination in self.list_of_v
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        assert source in self.list_of_v
        assert destination in self.list_of_v
        if edge == EdgeType.undirected:
            self.add_directed_edge(destination, source, weight)
        self.add_directed_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None], start: Optional[Vertex] = None) -> None:
        visited: list[Vertex] = []
        if start is None:
            v: Vertex = self.list_of_v[0]
        else:
            v: Vertex = start

        queue: Queue = Queue()
        queue.enqueue(v)
        while len(queue) != 0:
            tmp = queue.dequeue()
            if tmp not in visited:
                visit(tmp)
                visited.append(tmp)
                toq = self.adjacencies[tmp]
                for i in toq:
                    queue.enqueue(i.destination)

    def __dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        if v not in visited:
            visit(v)
            visited.append(v)
        for i in self.adjacencies[v]:
            if i.destination not in visited:
                self.__dfs(i.destination, visited, visit)

    def traverse_depth_first(self, visit: Callable[[Any], None], start: Optional[Vertex] = None) -> None:
        visited: list[Vertex] = []
        if start is None:
            v: Vertex = self.list_of_v[0]
        else:
            v: Vertex = start

        self.__dfs(v, visited, visit)

    def show(self):
        is_weighted: bool = False
        for i in self.adjacencies:
            for j in self.adjacencies[i]:
                if j.weight is not None:
                    is_weighted = True
                    break
        is_directed: bool = False
        if self.type_of_g == EdgeType.directed:
            is_directed = True

        g: igraph.Graph = igraph.Graph(directed=is_directed)
        for i in self.list_of_v:
            g.add_vertex(str(i.index))

        def ae(v: Vertex):
            for i in self.adjacencies[v]:
                g.add_edge(str(v.index), str(i.destination.index))
                if is_weighted:
                    tmp = g.get_eid(str(v.index), str(i.destination.index))
                    es = igraph.EdgeSeq(g)
                    es[tmp]["weight"] = i.weight
                    es[tmp]["label"] = str(i.weight)

        for i in self.list_of_v:
            ae(i)

        g.vs["label"] = g.vs["name"]
        g.vs["label_color"] = "black"
        g.vs["size"] = 20
        g.vs["color"] = "white"
        plot(g)
        return

    def find_paths(self, cv: Vertex, searched: Vertex, paths: list[Edge], visited: list[Vertex],
                   result: list[list[Edge]]):
        if cv == searched:
            if len(paths) != 0:
                result.append(paths.copy())
            return

        visited.append(cv)
        tmp = paths.copy()
        tmp2 = visited.copy()

        for i in self.adjacencies[cv]:
            if i.destination not in visited:
                paths.append(i)
                visited.append(i.destination)
                self.find_paths(i.destination, searched, paths, visited, result)
            paths = tmp
            visited = tmp2

    def find(self, a: Vertex, b: Vertex):
        result = []
        visited = []
        paths = []
        self.find_paths(a, b, paths, visited, result)
        # detect loops
        if a == b:
            for i in self.adjacencies[a]:
                if i.destination == i.source:
                    result.append(i)
        return result

    def __init__(self):
        self.idx = 0
        self.list_of_v = []
        self.adjacencies = {}
        self.type_of_g = EdgeType.undirected

    def __str__(self):

        to_print: list[str] = []

        for i in self.adjacencies:
            tmp: str = str(i.index) + ": " + str(i.data) + " -----> ["
            for j in self.adjacencies[i]:
                if tmp[-1] != "[":
                    tmp += ", "
                tmp += str(j.destination.index) + ": " + str(j.destination.data)
            tmp += "]"
            to_print.append(tmp)

        to_return: str = ""

        for i in to_print:
            to_return += i + "\n"

        return to_return
