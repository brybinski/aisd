from typing import Any, List, Callable, Union
from Lab02.Queue import Queue


class TreeNode:
    value: Any
    # Any to suppress warnings
    children: List[Any]
    parent: 'TreeNode'

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child: 'TreeNode'):
        self.children.append(child)
        child.parent = self

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for i in self.children:
            if i is not None:
                i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue: 'Queue' = Queue()

        for i in self.children:
            if i is not None:
                queue.enqueue(i)

        while len(queue) != 0:
            x = queue.dequeue()
            visit(x)
            for i in x.children:
                if i is not None:
                    queue.enqueue(i)

    def search(self, value: Any) -> Union['TreeNode', None]:
        result: List[TreeNode] = []

        def search_foo(node: 'TreeNode'):
            if node.value == value:
                result.append(node)

        self.for_each_level_order(search_foo)

        if len(result) == 0:
            return None
        else:
            return result[0]
        # #This is for more than one node if ever needed it
        # #ADD ", List['TreeNode']" to Union
        # elif len(result) == 1:
        #     return result[0]
        # else:
        #     return result

    def __init__(self, value: Any = None, parent: Any = None):
        self.value = value
        self.children = []
        self.parent = parent

    def __str__(self) -> str:
        return str(self.value)
