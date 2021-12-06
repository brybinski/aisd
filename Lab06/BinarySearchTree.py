import Lab05
from Lab05.BinaryNode import BinaryNode
from typing import Any, Callable, Optional, List
import treelib as tr
from igraph import *


class BinarySearchTree(Lab05.BinaryTree):
    root: BinaryNode

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


def f(a=10):
    return a * 10


x = BinarySearchTree(8)
x.insert(3)
x.insert(6)
x.insert(1)
x.insert(4)
x.insert(7)
x.insert(10)
x.insert(14)
x.insert(13)
x.show()
