from typing import Any, Callable, Optional, List, Tuple, Union
import matplotlib.pyplot as plt
from Lab02.Queue import Queue
from BinaryNode import BinaryNode
import treelib as tr
from igraph import *


class BinaryTree:
    root: BinaryNode

    def assign(self) -> List[Any]:
        iteration: List[int] = [0]
        tmp: List[int] = [0]

        result: List[('BinaryNode', int)] = []

        def add_record(node: 'BinaryNode'):
            if node is not None:
                result.append([node, iteration[0]])
                iteration[0] += 1

        self.traverse_in_order(add_record)
        return result

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self, label_color: str = "black", size: int = 30, color: str = "white") -> None:
        g = Graph(n=len(self), directed=True)

        vertices: List[Any] = self.assign()
        edge_list: List[Tuple] = []
        labels: List[str] = [""] * len(self)

        def add_e(node: 'BinaryNode') -> None:
            if node is not None:
                parent: int = [v[1] for v in vertices if v[0] == node][0]
                for i in node.left_child, node.right_child:
                    if i is not None:
                        child: int = [x[1] for x in vertices if x[0] == i][0]
                        edge_list.append((child, parent))
                labels[parent] = str(node.value)

        self.traverse_pre_order(add_e)

        g.vs["label"] = labels
        g.vs["label_color"] = label_color
        g.vs["size"] = size
        g.vs["color"] = color

        g.add_edges(edge_list)

        plot(g, layout=g.layout_reingold_tilford(mode="in", root=[i for i in vertices if i[0] == self.root][0][1]))

        # plot but for matplotlib instead of pycairo
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

tree.show()

assert tree.root.value == 10

assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True


def horizontal_sum(tree: BinaryTree) -> List[Any]:
    assigned: List[('BinaryNode', int)] = []

    # Here I am assigning each vertex of graph to a level
    def level_assignment(node: 'BinaryNode', level: int = 0) -> None:
        assigned.append((node, level))
        for i in node.left_child, node.right_child:
            if i is not None:
                level_assignment(i, level + 1)

    level_assignment(tree.root)

    max_level: int = 0
    for i in assigned:
        if i[1] > max_level:
            max_level = i[1]

    result: List[Any] = [None] * (max_level + 1)

    # I know this is longer than list comprehension
    # but it works for str flawlessly

    for i in range(0, max_level + 1):
        tmp: Any = None
        for ele in assigned:
            if ele[1] == i:
                if tmp is not None:
                    tmp += ele[0].value
                else:
                    tmp = ele[0].value

        result[i] = tmp
    return result


test_list = horizontal_sum(tree)
print(test_list)


def wypisz(node: 'BinaryNode'):
    print(node.value)


tree.traverse_in_order(wypisz)
