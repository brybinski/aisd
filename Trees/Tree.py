from typing import Any, List, Callable, Tuple
from igraph import *
from Trees.TreeNode import TreeNode


# pip install pycairo

class Tree:
    root: TreeNode

    def assign(self) -> List[Any]:
        iteration: List[int] = [0]
        tmp: List[int] = [0]

        result: List[('TreeNode', int)] = []

        def add_record(node: 'TreeNode'):
            if node is not None:
                result.append([node, iteration[0]])
                iteration[0] += 1

        self.for_each_level_order(add_record)
        return result

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

    def show(self, label_color: str = "black", size: int = 30, color: str = "white") -> None:
        g = Graph(n=len(self), directed=True)

        vertices: List[Any] = self.assign()
        edge_list: List[Tuple] = []
        labels: List[str] = [""] * len(self)

        def add_e(node: 'TreeNode') -> None:
            if node is not None:
                parent: int = [x[1] for x in vertices if x[0] == node][0]
                for i in node.children:
                    if i is not None:
                        child: int = [x[1] for x in vertices if x[0] == i][0]
                        edge_list.append((child, parent))
                labels[parent] = str(node.value)

        self.for_each_level_order(add_e)

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

    def __init__(self, value=None):
        self.root = TreeNode(value)

    def __len__(self):
        count: List[int] = [0]

        def counter(node: 'TreeNode') -> None:
            count[0] += 1

        self.for_each_level_order(counter)

        return count[0]


# trr: 'Tree' = Tree('F')
# trr.root.add(TreeNode('B'))
# trr.root.add(TreeNode('G'))
# trr.root.children[0].add(TreeNode('A'))
# trr.root.children[0].add(TreeNode('D'))
# trr.root.children[0].children[1].add(TreeNode('C'))
# trr.root.children[0].children[1].add(TreeNode('E'))
# trr.root.children[1].add(TreeNode('I'))
# trr.root.children[1].children[0].add(TreeNode('H'))
#
# trr.show()
