from Lab05.BinaryNode import BinaryNode
from typing import Any, Callable, Optional, List
import treelib as tr

class BinarySearchTree:
    root: BinaryNode

    def _insert(self, form: 'BinaryNode', val: Any) -> 'BinaryNode':
        if val < form.value:
            if form.left_child is not None:
                self._insert(form.left_child, val)
            else:
                form.add_left_child(val)
                return form.left_child

        if val >= form.value:
            if form.right_child is not None:
                self._insert(form.right_child, val)
            else:
                form.add_right_child(val)
                return form.right_child

    def insert(self, val):
        self._insert(self.root, val)

    # TODO: rewrite remove
    def _remove(self, node: BinaryNode, val: Any, before: 'Optional'=None):
        if node.value == val:
            if node.is_leaf():
                if before.value < node.value:
                    before.right_child = None
                    return
                else:
                    before.left_child = None
                    return

            if node.left_child is None:
                if before.value < node.value:
                    before.right_child = node.right_child
                    return
                else:
                    before.left_child = node.right_child
                    return

            if node.right_child is None:
                return None

            self.insert(node.value)

            node = node.left_child
            node = node.right_child
            if node.right_child is not None:
                self._remove(node.right_child, val, before=node)

        if node.value < val and node.right_child is not None:
            self._remove(node.right_child, val, before=node)

        if node.value > val and node.left_child is not None:
            self._remove(node.left_child, val, before=node)

        return node

    def remove(self, val: Any) -> None:
        self._remove(self.root, val)

    def insertlist(self, list: List[Any]) -> None:
        for i in list:
            self.insert(i)

    # TODO: Better show
    def show(self) -> None:
        g = tr.Tree()

        g.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                g.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child is not None:
                g.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.root.traverse_pre_order(add_edge)
        g.show()

    def contains(self, value) -> bool:
        res: List[bool] = [False]

        def compare(node: BinaryNode) -> None:
            if node.value == value:
                res[0] = True

        self.root.traverse_pre_order(compare)
        return res[0]

    def __init__(self, value: Optional = None, root: BinaryNode = None) -> None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root


x = BinarySearchTree(3)
x.insertlist([2, 5, 6, 1, 8, 4])
print(x.contains(2))
print(x.contains(9))
x.show()
