from typing import Any, Callable, Optional
from Lab05.BinaryNode  import BinaryNode
import treelib as tr


class BinaryTree:
    root: BinaryNode

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        g = tr.Tree()

        g.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                g.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child is not None:
                g.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.traverse_pre_order(add_edge)
        g.show()

    def __init__(self, value: Optional = None, root: BinaryNode = None) -> None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root


x: BinaryNode = BinaryNode(10)
x.add_left_child(9)
x.add_right_child(2)
x.left_child.add_left_child(1)
x.left_child.add_right_child(3)
x.right_child.add_left_child(4)
x.right_child.add_right_child(6)

tree: BinaryTree = BinaryTree(root=x)

tree.show()

assert tree.root.value == 10

assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
