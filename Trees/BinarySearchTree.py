from typing import Any, Optional, Callable, List
from Trees.BinaryTree import *


class BinarySearchTree(BinaryTree):

    def _insert(self, form: 'BinaryNode', val: Any):
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

    def _remove(self, value):
        return

    def remove(self, val):
        self._remove(val)

    def __init__(self):
        super().__init__()
