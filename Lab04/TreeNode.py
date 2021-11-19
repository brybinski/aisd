from typing import Any, List, Callable, Union
from Lab02.Queue import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child: 'TreeNode'):
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue: 'Queue' = Queue()

        for i in self.children:
            queue.enqueue(i)

        while len(queue) != 0:
            x = queue.dequeue()
            visit(x)
            for i in x.children:
                queue.enqueue(i)

    def search(self, value: Any) -> Union['TreeNode', List['TreeNode'], None]:
        result: List[TreeNode] = []

        def search_foo(node: 'TreeNode'):
            if node.value == value:
                result.append(node)

        self.for_each_level_order(search_foo)

        if len(result) == 0:
            return None
        elif len(result) == 1:
            return result[0]
        # else:        # This is for more than one node
        #     return result

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)


# Tests
tree: 'TreeNode' = TreeNode(2)

tree.add(TreeNode(1))

tree.add(TreeNode(4))

tree.children[0].add(TreeNode(3))

tree.children[1].add(TreeNode(6))


def foo(tre: 'TreeNode'):
    print(tre.value)
