from typing import Any, Callable, Optional, List
from Trees.TreeNode import TreeNode


class BinaryNode(TreeNode):

    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    color: bool

    def add(self, value) -> None:
        return None

    def min(self) -> 'BinaryNode':
        if self.children[0] is not None and self.children[1] is not None:
            if self.children[0].value > self.children[1].value:
                return self.children[1]
            else:
                return self.children[0]
        elif self.children[0] is not None:
            return self.children[0]
        elif self.children[1] is not None:
            return self.children[1]
        else:
            return None

    def add_left_child(self, value: Any) -> None:
        self.children[0] = BinaryNode(value)
        self.left_child = self.children[0]

    def add_right_child(self, value: Any) -> None:
        self.children[1] = BinaryNode(value)
        self.right_child = self.children[1]

    def is_leaf(self) -> bool:
        if (self.children[1] is None) and (self.children[0] is None):
            return True
        else:
            return False

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.children[0] is not None:
            self.children[0].traverse_in_order(visit)
        visit(self)
        if self.children[1] is not None:
            self.children[1].traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.children[0] is not None:
            self.children[0].traverse_post_order(visit)
        if self.children[1] is not None:
            self.children[1].traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.children[0] is not None:
            self.children[0].traverse_pre_order(visit)
        if self.children[1] is not None:
            self.children[1].traverse_pre_order(visit)

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

    def __init__(self, value: Optional=None):
        super().__init__(value)
        self.children.append(None)
        self.children.append(None)
        self.right_child = self.children[1]
        self.left_child = self.children[0]

