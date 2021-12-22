import math
import random
from heapq import heappop, heappush
from typing import List
from GraphInterface import GraphInterface
import json
import matplotlib.pyplot as plt
from DiGraph import DiGraph


class GraphAlgo:
    # constructor
    def __init__(self, g: GraphInterface = DiGraph()) -> None:
        self._graph = g

    # return: the directed graph on which the algorithm works on.
    def get_graph(self) -> GraphInterface:
        return self._graph

    #  Loads a graph from a json file.
    def load_from_json(self, file_name: str) -> dict:
        new = DiGraph()
        try:
            with open(file_name, "r") as file:
                g = json.load(file)
                # Adds all the Nodes
                for i in g.get("Nodes"):
                    # If the POS exists
                    if "pos" in i and len(i.get("pos")) != None:
                        Pos = []
                        current = i.get("pos")
                        cnt = current.split(',')
                        for k in cnt:
                            Pos.append(float(k))
                        new.add_node(int(i.get("id")), tuple(Pos))
                    # If the POS not exists
                    else:
                        new.add_node(int(i.get("id")))
                # Adds all the Edges
                for i in g.get("Edges"):
                    new.add_edge(int(i.get("src")), int(i.get("dest")), float(i.get("w")))
            self._graph = new
            return True

        except IOError as e:
            print(e)
            return False

    # Saves the graph in JSON format to a file
    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                ans = {}
                nodes = []
                edges = []
                # If the POS exists
                if self._graph.get_all_v()[0].getLocation() is not None:
                    ans["Edges"] = edges
                    ans["Nodes"] = nodes
                # If the POS not exists
                else:
                    # Add all the things to the file
                    ans["Nodes"] = nodes
                    ans["Edges"] = edges
                # Adds all the Nodes
                for i in self._graph.get_all_v().values():
                    # If the POS exists
                    if i.getLocation() is not None:
                        nodes.append({"id": i.getKey(), "pos": str(
                            str(i.getLocation()[0]) + "," + str(i.getLocation()[1]) + "," + str(i.getLocation()[2]))})
                    # If the POS not exists
                    else:
                        nodes.append({"id": i.getKey()})
                    # Adds all the edges
                    for dest, w in self._graph.all_out_edges_of_node(i.getKey()).items():
                        if self._graph.get_all_v()[0].getLocation() is not None:
                            edges.append({"src": i.getKey(), "w": w, "dest": dest})
                        else:
                            edges.append({"src": i.getKey(), "dest": dest, "w": w})
                json.dump(ans, indent=2, fp=file)
                return True

        except IOError as e:
            print(e)
            raise False

    # Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        final_dist = {}
        cnt = []
        all_v = self._graph.get_all_v().keys()
        # Checks if the src exists
        if id1 not in all_v:
            return float('inf'), []
        # Checks if the dest exists
        if id2 not in all_v:
            return float('inf'), []
        dic_path = {id1: [id1]}
        visit = {id1: 0}
        heappush(cnt, (0, id1))
        # As long as cnt not empty
        while len(cnt):
            (dist, node) = heappop(cnt)
            # If we have already gone over the node
            if node in final_dist:
                pass
            final_dist[node] = dist
            # If we have finished the calculation
            if node == id2:
                # If the path exists
                if id2 in final_dist and id2 in dic_path:
                    return final_dist[id2], dic_path[id2]
                # If the path not exists
                else:
                    return float('inf'), []
                # If the process of finding the route is not over yet
            for dest, w in self._graph.all_out_edges_of_node(node).items():
                the_dist = final_dist[node] + w
                # Adding the weight of the edge to the track
                if dest not in visit or the_dist < visit[dest]:
                    # Add the node to the placement of the node we visited
                    visit[dest] = the_dist
                    heappush(cnt, (the_dist, dest))
                    if node not in dic_path:
                        # Add the node to the path
                        dic_path[node] = node
                    dic_path[dest] = dic_path[node] + [dest]
        return float('inf'), []

    #Finds the shortest path that visits all the nodes in the list
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        # if the list is empty
        if len(node_lst)==0:
            return None , None

        #the ans path
        Path = []
        j=0
        id1=node_lst[j]

        # if we need to go to one node
        if len(node_lst)==1:
            #return this node
            Path.append(self._graph.get_all_v()[id1])
            return Path , 0

        w=0
        #Go over any pair of nodes
        for i in range(0,len(node_lst)-1):
            id1 = node_lst[i]
            id2 = node_lst[i+1]
            cnt = self.shortest_path(id1,id2)[1]
            #the ans weigth
            w += self.shortest_path(id1,id2)[0]
            if i>0:
                cnt.remove(cnt[0])
            Path.extend(cnt)

        return Path, w



    # Finds the node that has the shortest distance to it's farthest node.
    def centerPoint(self) -> (int, float):
        # create Node that will return the answer
        ans = None
        ans_w = math.inf
        for i in range(0, self._graph.v_size()):
            current = 0
            for j in range(0, self._graph.v_size()):
                # for node i we calculate all the paths to the other nodes
                w = self.shortest_path(i, j)[0]
                # Keeps the longest path
                if current < w:
                    current = w
            # save the shortest path
            if current < ans_w:
                ans_w = current
                ans = self._graph.get_all_v()[i]

        return ans.getKey(), ans_w

    # Taken from Amichai's lesson
    # Plots the graph.
    # If the nodes have a position, the nodes will be placed there.
    # Otherwise, they will be placed in a random but elegant manner.
    def plot_graph(self) -> None:
        # Adds all the Nodes
        for v in self._graph.get_all_v().values():
            # If it does not exist Location then adds Location randomly
            if v.getLocation() is None:
                x, y = random.uniform(0.0, 100), random.uniform(0.0, 100)
                pos = (x, y, 0)
                v.setLocation(pos)
            # If it does exist Location
            x, y, z = v.getLocation()
            plt.plot(x, y, markersize=10, marker='o', color='pink')
            plt.text(x, y, str(v.getKey()), color="black", fontsize=11)
            # Adds all the Edge
            for i, d in self._graph.all_out_edges_of_node(v.getKey()).items():
                node = self._graph.get_all_v()[i]
                # If it does not exist Location then adds Location randomly
                if node.getLocation() is None:
                    his_x, his_y = random.uniform(0.0, 100), random.uniform(0.0, 100)
                    pos = (his_x, his_y, 0)
                    node.setLocation(pos)
                # If it does exist Location
                his_x, his_y, his_z = node.getLocation()
                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))

        plt.show()


