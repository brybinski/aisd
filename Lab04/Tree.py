from typing import Any, List, Callable
from Lab04.TreeNode import TreeNode
import networkx as nx
import matplotlib.pyplot as plt


class Tree:
    root: TreeNode

    def add(self, value: Any, parent_name: 'TreeNode') -> None:

        is_present: List[bool] = [False]

        def search_nodes(node: 'TreeNode') -> None:
            if node == parent_name:
                is_present[0] = True

        self.root.for_each_level_order(search_nodes)

        if is_present[0]:
            parent_name.add(value)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        G = nx.Graph()

        def add_node(node: 'TreeNode') -> None:
            G.add_node(node.value)


        def add_edge(node: 'TreeNode') -> None:
            for i in node.children:
                G.add_edge(node.value, i.value)

        self.for_each_deep_first(add_node)
        self.for_each_deep_first(add_edge)

        plt.subplot(121)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        # TODO: igraph instead of networkx

    def __init__(self, value=None):
        self.root = TreeNode(value)

    def __len__(self):
        count: List[int] = [0]

        def counter() -> None:
            count[0] += 1

        self.for_each_level_order(counter)

        return counter


trr: 'Tree' = Tree('F')
trr.root.add(TreeNode('B'))
trr.root.add(TreeNode('G'))
trr.root.children[0].add(TreeNode('A'))
trr.root.children[0].add(TreeNode('D'))
trr.root.children[0].children[1].add(TreeNode('C'))
trr.root.children[0].children[1].add(TreeNode('E'))
trr.root.children[1].add(TreeNode('I'))
trr.root.children[1].children[0].add(TreeNode('H'))


def foo(tre: 'TreeNode'):
    print(tre.value)


trr.for_each_level_order(foo)

trr.show()
