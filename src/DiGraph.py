from Node import NodeDataImpl

class DiGraph:
    # constructor
    def __init__(self) -> None:
        self._Nodes = {}
        self._Edges = {}
        self._Node_Size = len(self._Nodes)
        self._Edge_Size =len(self._Edges)
        self._MC = 0

    # Convert DiGraph to STR
    def __str__(self) -> str:
        return f"Graph: |V|= {self.v_size()} , |E|= {self.e_size()}"

    # Convert DiGraph to STR
    def __repr__(self) -> str:
        return f"Graph: |V|= {self.v_size()} , |E|= {self.e_size()}"

   # Returns the number of node in this graph
    def v_size(self) -> int:
        return self._Node_Size

   # Returns the number of edges in this graph
    def e_size(self) -> int:
        return self._Edge_Size

   #return a dictionary of all the nodes in the Graph, each node is represented using a pair
    def get_all_v(self) -> dict:
        return self._Nodes

   #return a dictionary of all the nodes connected to (into) node_id
    def all_in_edges_of_node(self, id1: int) -> dict:
        all_v = {}
        for i, t in self._Edges.items():
           #t is the DEST
           #If id1 is DEST you will add the edge
            if id1 in t:
                all_v[i] = t[id1]
        return all_v

   #return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._Edges[id1]

   # Returns the current version of this graph
    def get_mc(self) -> int:
        return self._MC

  #   Adds an edge to the graph
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self._Nodes and id2 in self._Nodes and id2 not in self._Edges[id1]:
           #Adds if the edge does not exist
            if self._Edges[id1] is None:
                self._Edges[id1] = {}
                self._Edges[id1][id2] = weight

            else:
                self._Edges[id1][id2] = weight
            #Changes the data of the graph according to the edge we added
            self._MC += 1
            self._Edge_Size += 1
            self._Nodes[id1].edge_out +=1
            self._Nodes[id2].edge_in += 1
            return True
        else:
            #If the edge was present it only changes the weight
            if id2 in self._Edges[id1]:
                self._Edges[id1][id2] = weight
                return True
        return False


   # Adds a node to the graph.
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self._Nodes:
             #If the node does not exist
            node = NodeDataImpl(_key=node_id, _Location=pos)
            self._Nodes[node_id] = node
            self._Edges[node_id] = {}
             # Changes the data of the graph according to the node we added
            self._MC += 1
            self._Node_Size += 1
            return True
        #If the node does exist
        else:
         self.get_all_v()[node_id].setLocation(pos)
         return True

    # Removes a node from the graph.
    def remove_node(self, node_id: int) -> bool:
        # If the node does not exist
        if node_id not in self._Nodes:
            return False
        # If the node does  exist
        self._MC =  self._MC + len(self._Edges[node_id])
        #Deletes all edges that in the node
        self._Edge_Size = self._Edge_Size - len(self._Edges[node_id])
        out = self.all_in_edges_of_node(node_id)
        del (self._Edges[node_id])
        for i in out.keys():
            # Deletes all edges that out the node
            self.remove_edge(i, node_id)
        # Changes the data of the graph according to the edge we Deletes
        self._Nodes.pop(node_id)
        self._MC += 1
        self._Node_Size -= 1
        return True

  # Removes an edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        #If the edge exists
        if node_id1 in self._Nodes and node_id2 in self._Nodes and node_id2 in self._Edges[node_id1]:
            #Deletes the Edge
            self._Edges[node_id1].pop(node_id2)
            # Changes the data of the graph according to the edge we Deletes
            self._Edge_Size -= 1
            self._MC += 1
            self._Nodes[node_id1].edge_out -= 1;
            self._Nodes[node_id2].edge_in -= 1;
            return True
        return False




