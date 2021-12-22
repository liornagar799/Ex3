import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def new(self) -> DiGraph:
            graph1 = DiGraph()
            graph1.add_node(0)
            graph1.add_node(1)
            graph1.add_node(2)
            graph1.add_node(3)
            graph1.add_node(4)
            graph1.add_edge(0, 1, 1)
            graph1.add_edge(0, 4, 1)
            graph1.add_edge(1, 2, 1)
            graph1.add_edge(1, 3, 5)
            graph1.add_edge(2, 3, 2)
            graph1.add_edge(4, 3, 1)
            graph1.add_edge(4, 1, 2)
            return graph1

    def test_get(self):
        g = self.new()
        ga = GraphAlgo(g)
        self.assertEqual(ga.get_graph().e_size(), g.e_size())

    def test_shortest_path(self):
        g = self.new()
        ga = GraphAlgo(g)
        l = (2, [0, 4, 3])
        lst = ga.shortest_path(0, 3)
        self.assertEqual(l, lst)

    def test_tsp(self):
            graph2 = DiGraph()
            targets = [0, 1, 2]
            b = GraphAlgo(graph2)
            expected = [0,1,2];
            print(b.TSP(targets)[1])
            self.assertEqual(b.TSP(targets)[0], expected)


    def test_center_load(self):
        g = DiGraph()
        a = GraphAlgo(g)
        a.load_from_json("../data/A0.json")
        self.assertEqual(a.centerPoint()[0], 7)