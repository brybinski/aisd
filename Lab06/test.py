from typing import Callable, Any


class BinaryNode:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        if self.left_child is None:
            self.left_child = BinaryNode(value)
        else:
            print("This node already has a left child!")

    def add_right_child(self, value: Any):
        if self.right_child is None:
            self.right_child = BinaryNode(value)
        else:
            print("This node already has a right child")

    def treverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.treverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.treverse_in_order(visit)

    def treverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.treverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.treverse_post_order(visit)
        visit(self)

    def treverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.left_child.treverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.treverse_pre_order(visit)

    def printNode(self):
        if self.value is not None:
            print(self.value)
        else:
            print("Ludzie przecież tu nikogo nie ma")

class BinaryTree:
    def __init__(self, root):
        self.root: BinaryNode = BinaryNode(root)

    def treverse_in_order(self, visit: Callable[[Any], None]):
        if self.root.left_child is not None:
            self.root.left_child.treverse_in_order(visit)
        visit(self)
        if self.root.right_child is not None:
            self.root.right_child.treverse_in_order(visit)

    def treverse_post_order(self, visit: Callable[[Any], None]):
        self.root.treverse_post_order(visit)

    def treverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.root.left_child is not None:
            self.root.left_child.treverse_pre_order(visit)
        if self.root.right_child is not None:
            self.root.right_child.treverse_pre_order(visit)



tree = BinaryTree(10)
tree.root.add_right_child(2)
tree.root.add_left_child(9)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_right_child(6)
tree.root.right_child.add_left_child(4)

assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True


def wypisz(node: 'BinaryNode'):
    print(node.value)

tree.treverse_post_order(wypisz)
