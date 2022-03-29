from typing import Any, Callable, Optional, List, Tuple, Union
from BinaryNode import BinaryNode
from Trees.Tree import Tree
import sys


class BinaryTree(Tree):

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def __init__(self, value: Optional = None, root: BinaryNode = None) -> None:
        super().__init__(value)
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root


test_node: BinaryNode = BinaryNode(1)
test_node.add_left_child(2)
test_node.add_right_child(3)
test_node.left_child.add_left_child(4)
test_node.left_child.add_right_child(5)
test_node.left_child.left_child.add_left_child(8)
test_node.left_child.left_child.add_right_child(9)
test_node.right_child.add_right_child(7)


tree: BinaryTree = BinaryTree(root=test_node)
tree.show()


def horizontal_sum(tree: BinaryTree) -> List[Any]:
    result: List[Any] = []

    def recursive(node: 'BinaryNode', level: int = 0) -> None:
        if len(result) <= level:
            result.append(node.value)
        else:
            result[level] = result[level] + node.value
        for i in node.left_child, node.right_child:
            if i is not None:
                recursive(i, level + 1)

    recursive(tree.root)

    return result


test_list = horizontal_sum(tree)
print(test_list)
