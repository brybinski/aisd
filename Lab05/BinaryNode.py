from typing import Any, Callable, Optional


class BinaryNode:
    last_id: int = -1
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    id: int

    def min(self) -> 'BinaryNode':
        if self.left_child.value > self.right_child.value:
            return self.right_child
        else:
            return self.left_child

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def is_leaf(self) -> bool:
        if (self.right_child is None) and (self.left_child is None):
            return True
        else:
            return False

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    # noinspection PyTypeChecker
    def __init__(self, value: Optional = None) -> None:
        self.value = value
        self.right_child = None
        self.left_child = None
        self.id = BinaryNode.last_id +1
        BinaryNode.last_id += 1

    def __str__(self):
        return str(self.value)




