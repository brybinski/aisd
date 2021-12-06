import igraph as ig
g = ig.Graph(n = 12, directed=True)
g.add_edges([(1,0),(2,1), (3,2), (4,3),
             (5,1),
             (6,2), (7,6), (8,7), (9,0),
             (10,0), (11,10)])
g.vs["label"] = ["A", "B", "A", "B", "C", "F", "C", "B", "D", "C", "D", "F"]

ig.plot(g, layout = g.layout_reingold_tilford(mode="in", root=0))
