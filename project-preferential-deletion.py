
#def edgeIncident:

# Calculate the total edges in the graph by looking at the number
# of attached edges for each node
def getGraphEdges(G):

    edges = 0
    for n in G:
        edges+=len(G[n])

    return edges

# With probability p, a new nod is added to the grath, together with a new edge incident
def birthProcess(G, newNode):
    # create a new node with an edge attached

    currentHighProbablity = 0
    nodeToAttach = 1

    # If empty graph again
    if(len(G) == 0):
        G[1] = []
        return


    edges = getGraphEdges(G)

    # Find the node with the highest probablity of linear preferential attachem
    for n in G:

        if(len(G[n]) == 0):
            continue

        prob = len(G[n])/(2*edges)

        # if this is higher than the current, set this as the current node
        if(prob > currentHighProbablity):
            currentHighProbablity = prob
            nodeToAttach = n

    # Add the new node to the graph by attaching to the node with high prob to directed graph
    G[newNode] = [nodeToAttach]
    G[nodeToAttach].append(newNode)

def deathProcess(G):

    # Get the current number of nodes in G
    numNodes = len(G)
    if(len(G) == 1):
        return

    currentHighProbablity = 0
    nodeToDelete = 0

    for n in G:

        if(len(G[n]) == 0):
            continue

        du = len(G[n])

        prob = 1 - (((numNodes - du)/((du*du)) - (2*getGraphEdges(G))))
      
        if(prob < currentHighProbablity):
            currentHighProbablity = prob
            nodeToDelete = n

    # Remove each edge to the node
    if(nodeToDelete == 0):
        return
    for n in G[nodeToDelete]:          


        if n not in G:
            continue
        G[n].remove(nodeToDelete)
     
        if(len(G[n]) == 0):
            del G[n]

    del G[nodeToDelete]

def runModel( steps, pVal ):
    # Begin by defining a dynamic random graph with a single node
    Graph = { 1:[2,3,4,5], 2:[3], 3:[1,2], 4:[1], 5:[1] }
    nextNode = 2
    t = 0

    # In a self-loop of t + 1, t>0 eith run a birth proces or run a death process
    while t < steps:

        seed(datetime.now())
        p = random()
        q = 1 - p

        if(p > pVal):
            birthProcess(Graph, nextNode)
        elif(q > pVal):
            deathProcess(Graph)
        nextNode+=1
        t+=1
    return Graph

def printStats(p):
    
    avg = {}

    i = 1000
    j = 0
    while i <= 5000:
        avg[i] = []
        while j < 1:
            #print(str(i))
            G = runModel(i, p)
            avg[i].append(len(G[1]))
            j+=1
        print(str(i) + ' ' + str(sum(avg[i]) / len(avg[i])))
        i+=1000
        j=0
    # print average for run

    #print(avg)
    print('For a given p of ' + str(p) + ' there were average following number of edges in 1:')
    #print('10000: ' + str(sum(avg[10000]) / len(avg[10000])))
    #print('20000: ' + str(sum(avg[20000]) / len(avg[20000])))
    #print('30000: ' + str(sum(avg[30000]) / len(avg[30000])))
    #print('40000: ' + str(sum(avg[40000]) / len(avg[40000])))
    #print('50000: ' + str(sum(avg[50000]) / len(avg[50000])))

from random import seed
from random import random
from random import randint
from datetime import datetime


printStats(0.1)
printStats(0.4)
printStats(0.9)

#m,G = runModel(10, 0.4)
#print(G)

