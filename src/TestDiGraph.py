from unittest import TestCase
from DiGraph import DiGraph


class TestDiGraph(TestCase):
    def new(self) -> DiGraph:
        graph1 = DiGraph()
        graph1.add_node(0)
        graph1.add_node(1)
        graph1.add_node(2)
        graph1.add_node(3)
        graph1.add_node(4)
        graph1.add_edge(0, 2, 1)
        graph1.add_edge(1, 2, 2)
        graph1.add_edge(2, 0, 3)
        graph1.add_edge(2, 3, 4)
        graph1.add_edge(3, 1, 5)
        graph1.add_edge(3, 4, 6)
        return graph1

    def test_add_node(self):
        g = self.new()
        self.assertEqual(5, g.v_size())
        g.add_node(10)
        self.assertEqual(6, g.v_size())

    def test_v_size(self):
        g = self.new()
        self.assertEqual(6, g.v_size())
        g.remove_node(10)
        self.assertEqual(5, g.v_size())

    def test_e_size(self):
        g = self.new()
        self.assertEqual(6, g.e_size())
        g.remove_node(0)
        self.assertEqual(3, g.e_size())


    def test_all_in_edges_of_node(self):
        lst = []
        g = self.new()
        l=[0,2]
        for i in g.all_in_edges_of_node(3).keys():
            lst.append(i)
        self.assertEqual(l,lst)


    def test_add_edge(self):
        g = self.new()
        self.assertEqual(6, g.e_size())
        g.add_edge(0,3,5)
        self.assertEqual(7, g.e_size())


    def test_remove_node(self):
        g = self.new()
        v=g.v_size()
        g.remove_node(1)
        self.assertEqual(v-1, g.v_size())


    def test_remove_edge(self):
        g = self.new()
        e=g.e_size()
        g.remove_edge(2,0)
        self.assertEqual(e-1, g.e_size())
