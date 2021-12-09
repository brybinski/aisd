from typing import Any, List, Callable
from igraph import *
from Lab04.TreeNode import TreeNode
import treelib as tr


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
        G = tr.Tree()


        G.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'TreeNode') -> None:
            for i in node.children:
                G.create_node(str(i.value), str(i.value), parent=str(node.value))

        self.for_each_level_order(add_edge)

        G.show()

        g = Graph()
        layout = g.layout("tree")

        def add_e(node: 'TreeNode') -> None:
            for i in node.children:
                g.add_edge(node.value, i.value)

        self.for_each_level_order(add_e)

        plot(g, layout=layout)

    def __init__(self, value=None):
        self.root = TreeNode(value)

    def __len__(self):
        count: List[int] = [0]

        def counter(node: 'TreeNode') -> None:
            count[0] += 1

        self.for_each_level_order(counter)

        return count[0]


trr: 'Tree' = Tree('F')
trr.root.add(TreeNode('B'))
trr.root.add(TreeNode('G'))
trr.root.children[0].add(TreeNode('A'))
trr.root.children[0].add(TreeNode('D'))
trr.root.children[0].children[1].add(TreeNode('C'))
trr.root.children[0].children[1].add(TreeNode('E'))
trr.root.children[1].add(TreeNode('I'))
trr.root.children[1].children[0].add(TreeNode('H'))

print(str(len(trr)))

