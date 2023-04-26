import networkx as nx
from matplotlib import pyplot as plt
import osmnx as ox
import numpy as np

G = nx.grid_2d_graph(5,5)

plt.figure(figsize=(7,7))
pos = {(x,y):(y,-x) for x,y in G.nodes()}
#  plot network
nx.draw(G, pos=pos, 
        node_color='lightgreen', 
        with_labels=True,
        node_size=600)

#  generate shortested path
orig= list(G)[0]
dest= list(G)[19]
route = nx.shortest_path(G, orig, dest, weight="length")

# draw shortested path
path_edges = list(zip(route,route[1:]))
nx.draw_networkx_nodes(G,pos,nodelist=route,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)

# generate agents group I
x = [round(np.random.uniform(0, 0.5),3) for i in range(50)]
y = [round(np.random.uniform(0, -0.5),3) for i in range(50)]

# generate agents group II
x1 = [round(np.random.uniform(3.5, 4),3) for i in range(20)]
y1 = [round(np.random.uniform(-2.5, -3),3) for i in range(20)]


# define nodes' property
class Node:
    """
    Object to simulate a network node
    """
    def __init__(self, NodeID, Poputation, Attractions, position):
            self.NodeID=NodeID
            self.Poputation=Poputation
            self.Attractions=Attractions
            self.position=position

# initialize nodes
Position=[]
for Pos in G.nodes(data=True):
        Position.append(Pos[0])

NodesSet=[]
for i in range(len(G.nodes)):
       Ins=Node(i,2,3,Position[i])
       NodesSet.append(Ins)
      
# define gravity model 
def gravitymodel(i,j,Poputation,Attractions,distance):
        G=(Poputation*Attractions)/(distance*distance)
        return G




plt.scatter(x, y, c ="blue", s = 10)
plt.scatter(x1, y1, c ="black", s = 10)
plt.show()



