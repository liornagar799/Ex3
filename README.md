# Ex3
The goal of this program to planning and realizing intentional and weighted graphs in python
# introduction:
The project is actually the design and implementation of directed and weighted graphs in the python programming language.
First, we had to design and implement four interfaces that were designed to produce a directed graph: class for nodes and class for graph.
Second, we implemented an interface of the algorithms of the graph, the breakdown of the function names and explanations will appear below.
Next, we implemented a graphical interface that Displays the graph.
We wrote UnitTesting to implement the functions of the graph and the algorithms of the graph, which are designed to test their correctness and performance.

## Planning of the main departments:

**Node** represents the set of operations applicable on a node in a weighted graph.

**DiGraph**This class implement #GraphInterface interface:The interface has a road-system or communication network in mind and should support a large number of nodes (over 100,000).
The GraphInterface class represents a Directional Weighted Graph,with effective representation.
**implementaion:**
We implemented the graph for the nodes and Edges we did using the data structure: dictionary.

## algorithems:

**GraphAlgo** This class implement GraphAlgoInterface interface, represents a Directed (positive) Weighted Graph Theory Algorithms.
The functions we implement:

 1. void **init**(GraphInterface g)- initialize the graph on which this set of the algorithms.
 2. GraphInterface **getGraph**()- returns the graph of this class.  
 3. **shortestPath**-return the weight of the path, and list of shortest path between src to dest, , if there is no path we return float('inf'), []
 4. **center**()-  Finds the Node with the shortest route to all other nodes.
 5. **tsp**(List<int> node_lst)- return a list of consecutive nodes which go over all the nodes in cities.
 6. **save**(file)- saves this weighted (directed) graph to the given, the file is JSON format.
 7. **load**(file)- loads a graph to this graph algorithm, the file is JSON format.
 8. **plot_graph**()- implemented a graphical interface that Displays the graph.
 

 
 ## Performence
 We tested the program we built with several different sizes of graphs.
 And compare it to the performance versus the same work in java.
 All comparisons can be found in the wiki file.
