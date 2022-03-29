from typing import Optional
from Vertex import Vertex
from EdgeType import EdgeType


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    edge_type: EdgeType

    def __init__(self, source: Vertex, destination: Vertex, edge_type: EdgeType, weight: Optional[float] = None):
        self.edge_type = edge_type
        for i in source, destination:
            if i is None:
                raise ValueError
        self.weight = weight
        self.source = source
        self.destination = destination

    def __str__(self):
        return "[" + str(self.source.index) + ": " \
               + str(self.source.data) + "]-----> [" \
               + str(self.destination.index) + ": " + str(self.destination.data) + "]"
