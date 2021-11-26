from Lab05.BinaryNode import BinaryNode
from typing import Any, Callable, Optional


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

    def __init__(self, value: Optional = None, root: BinaryNode = None) -> None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root


x = BinarySearchTree(3)
