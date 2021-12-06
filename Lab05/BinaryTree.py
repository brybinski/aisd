from typing import Any, Callable, Optional, List, Tuple, Union
import matplotlib.pyplot as plt
from Lab02.Queue import Queue
from BinaryNode import BinaryNode
import treelib as tr
from igraph import *


class BinaryTree:
    root: BinaryNode

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        G = tr.Tree()

        G.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                G.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child is not None:
                G.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.traverse_pre_order(add_edge)

        G.show()

        g = Graph(n=len(self), directed=True)

        edge_list: List[Tuple] = []
        ver: List[int] = []
        labels: List[str] = [""] * len(self)

        def add_e(node: 'TreeNode') -> None:
            if node.left_child is not None:
                edge_list.append((node.left_child.id, node.id))
            if node.right_child is not None:
                edge_list.append((node.right_child.id, node.id))
            ver.append(node.id)
            labels[node.id] = str(node.value)

        self.traverse_pre_order(add_e)

        g.vs["label"] = labels
        g.vs["label_color"] = "black"
        g.vs["size"] = 30
        g.vs["color"] = "white"
        print(edge_list)
        g.add_edges(edge_list)

        plot(g, layout=g.layout_reingold_tilford(mode="in", root=0))

        # pycairo is much better than matplotlib
        # fig, ax = plt.subplots()
        # lay = g.layout_reingold_tilford(mode="in", root=0)
        # lay.rotate(180)
        # plot(g, layout=lay, target=ax)
        # plt.show()

    def __init__(self, value: Optional = None, root: BinaryNode = None) -> None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root

    def __len__(self) -> int:
        count: List[int] = [0]

        def co(node):
            count[0] += 1

        self.traverse_in_order(co)
        return count[0]


x: BinaryNode = BinaryNode(10)
x.add_left_child(9.)
x.add_right_child(2)
x.left_child.add_left_child(1)
x.left_child.add_right_child(3)
x.right_child.add_left_child(4)
x.right_child.add_right_child(6)

tree: BinaryTree = BinaryTree(root=x)

#tree.show()

assert tree.root.value == 10

assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True


def horizontal_sum(tree: BinaryTree) -> List[Any]:
    tmp: List[('BinaryNode', int)] = []

    def levelAssignment(node: 'BinaryNode', level: int = 0) -> None:
        tmp.append((node, level))
        for i in node.left_child, node.right_child:
            if i is not None:
                levelAssignment(i, level + 1)

    levelAssignment(tree.root)

    max_level: int = 0
    for i in tmp:
        if i[1] > max_level:
            max_level = i[1]

    result: List[Any] = [tmp[0][0].value - tmp[0][0].value] * (max_level + 1)
    for i in tmp:
        result[i[1]] += i[0].value

    return result


test_list = horizontal_sum(tree)
print(test_list)
