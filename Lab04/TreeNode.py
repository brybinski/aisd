from typing import Any, List, Callable, Union
from Lab02.Queue import Queue


class TreeNode:

    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any):
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)

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

    def for_each_level_order(self, visit: Callable[['TreeNode'], None], first=True) -> None:
        queue: 'Queue' = Queue()

        if first:
            queue.enqueue(self)

        for i in self.children:
            queue.enqueue(i)

        for i in self.children:
            i.for_each_level_order(visit, False)

    def search(self, value: Any) -> Union['TreeNode', None]:
        result: List[TreeNode] = []
        def foo():
            if self.value == value:
                result.append(self)

        self.for_each_level_order(x)

        if len(result) == 0:
            return None
        else:
            return result


# Tests
tree: 'TreeNode' = TreeNode(2)

tree.add(TreeNode(1))

tree.add(TreeNode(4))

tree.children[0].add(TreeNode(3))

tree.children[1].add(TreeNode(6))


def foo(tree: 'TreeNode'):
    print(tree.value)


x = foo
tree.for_each_deep_first(x)

print('\n')

tree.for_each_level_order(x)

print(tree.search(4))