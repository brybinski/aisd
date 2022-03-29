from typing import Any, Optional


class Vertex:
    data: Any
    index: int
    _newidx: int = 0

    def __init__(self, data: Optional = None):
        self.data = data
        self.index = Vertex._newidx
        Vertex._newidx += 1
