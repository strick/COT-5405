import random
from random import randint
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
import operator

# This is based on an undirected graph, referred to the papter
# This is why you divide by 2

start_graph={1:[2,3,4],2:[1],3:[1,4],4:[1,3]}

Graph={1:[2,3,4],2:[1],3:[1,4],4:[1,3]}
#keys are the nodes 
#values are the nodes connected the key which is a node


def probability_birth(node):

	# for a given node calculate the degree of it.  Get the number of outgoing and incoming??? for 
	# the given node
	degree= len(Graph[node])

	#this should be called total degree
	edges=0

	# calculate total edges of the graph
	for i in Graph:
		#degree+=
		edges+=len(Graph[i])
		
	# Shouldn't have to do "ceil" or /2 if you're using directed graphs
	edges=math.ceil(edges/2)
	# if edges==0:
	# 	return 0

	# Return the probablility (degree of that specific node / total degree of the graph)
	# refer to formula (1) of paper
	return (degree)/(2*(edges))


# Total number of nodes - degree of previous node) / current count of nodes ^ 2 - total degree of Graph )2M_t
# this makes small degree nodes more likely canidates because 

# use 1/dt(u) to amke it more likely for "large degree" nodes to be likely canidates

def probability_death(node):

	number_of_nodes=len(Graph)
	degree= len(Graph[node])
	edges=0

	for i in Graph:
		edges+=len(Graph[i])

	edges=math.ceil(edges/2)	

	# Refer to forumula (2) of paper
	return ((number_of_nodes)-degree)/(((number_of_nodes)**2)-(edges*2))


def cummulative_probability(probability_of_nodes):

	if len(probability_of_nodes)==1:
		return probability_of_nodes

	else:
		# Look at all nodes in the probability list
		for i in range(1,len(probability_of_nodes))

			probability_of_nodes[i]+=probability_of_nodes[i-1]

		return probability_of_nodes


def birth_process():

	probability_of_nodes = []
	selected_node=0
	 
	 # Look at all the nodes in the grap and determine the probablility 
	for node in Graph:
		# obtain an ordered list of probabilities for each node
		probability_of_nodes.append(probability_birth(node))

	#create a cummlative prob list so there is some randomization of which node
	# gets to give birth.
	cummulative_prob_list = cummulative_probability(probability_of_nodes)

	#print(cummulative_prob_list)

	# Create the node number to brith based on the key because a node could be deleted
	# which won't allow len(graph)+1.
	new_node=max(Graph.keys())+1
	
	#edge_prob = random.uniform(0, max(cumulated_prob))
	# Get the list of current graph nodes
	list_of_keys=list(Graph.keys())

	# No bell curve, same likely hood you could get .1 .4, etct up to 1
	temp=random.uniform(0,max(cummulative_prob_list))


	# Figure out which node gets a birth attachment.
	for i in range(len(cummulative_prob_list)):
		#print("rand")
		#print(len(cummulative_prob_list))
		# If the super random number, temp, is less than the current cumlative prob
		if temp<cummulative_prob_list[i]:
			selected_node = list_of_keys[i]
			break
	# print(selected_node)
	
	# print(cumulated_prob)
	# print(probs)
	# print("Sum = ", sum(probs))

	# Create an edge from the new node to the selected node found based on cummlative
	# properties
	Graph[new_node]=[selected_node]   # new_node -> selected
	# Create the two way undirected graph binding   
	Graph[selected_node].append(new_node)   # selected -> new_node


def death_process():

	probability_of_nodes=[]
	list_of_keys=list(Graph.keys())

	for node in Graph:

		probability_of_nodes.append(probability_death(node))

	selected_node= list_of_keys[probability_of_nodes.index(max(probability_of_nodes))]


	for i in Graph[selected_node]:

		Graph[i].remove(selected_node)
		if len(Graph[i])==0:
			del Graph[i]

	del Graph[selected_node]


num_of_nodes_1=[]
num_of_nodes_2=[]
num_of_nodes_3=[]

num_of_edges_1=[]
num_of_edges_2=[]
num_of_edges_3=[]


Graph={1:[2,3,4],2:[1],3:[1,4],4:[1,3]}
#print(Graph)

# For p = 0.6
#print("p=0.6")
# Doing 10,000 possible additions and deletions
for t in range(0, 10000):

	# Create a random probabliliy
	r = randint(1,10)

	# if no graph, then create from the var start_graph
	if len(Graph)==0:
		Graph=start_graph

	# 60% birth 
	if r in range(1,7):
		#print("Birth")
		birth_process()

	# 40% death
	elif r in range(7,11):
		#print("Death")
		death_process()

	print("\n")
	print(t)
	# Get t
	if t%2500==0:
		num_of_nodes_1.append(len(Graph))	# For Graph nodes
		#print(num_of_nodes_1)
		#print("efk")
		edges=0
		# Calculate the total degree of the graph 
		for i in Graph:
			# change edges to degree
			edges+=len(Graph[i])

		# Total Degree / 2 = to number of edges 
		edges=math.ceil(edges/2)
		num_of_edges_1.append(edges)


Graph={1:[2,3,4],2:[1],3:[1,4],4:[1,3]}
#print(Graph)

# For p = 0.75
#print("p=0.75")
for t in range(0, 10000):
	r = randint(1,100)

	if len(Graph)==0:
		Graph=start_graph

	if r in range(1,76):
		#print("Birth")
		birth_process()

	elif r in range(76,101):
		#print("Death")
		death_process()

	print("\n")
	print(t)
	if t%2500==0:
		num_of_nodes_2.append(len(Graph))	# For Graph nodes
		#print(num_of_nodes_2)
		#print("efk")
		edges=0
		for i in Graph:
			edges+=len(Graph[i])

		edges=math.ceil(edges/2)
		num_of_edges_2.append(edges)


		
Graph={1:[2,3,4],2:[1],3:[1,4],4:[1,3]}
#print(Graph)

# For p = 0.9
#print("p=0.9")
for t in range(0, 10000):
	r = randint(1,10)

	if len(Graph)==0:
		Graph=start_graph

	if r in range(1,10):
		#print("Birth")
		birth_process()

	elif r in range(10,11):
		#print("Death")
		death_process()

	print("\n")
	print(t)
	if t%2500==0:
		num_of_nodes_3.append(len(Graph))	# For Graph nodes
		#print(num_of_nodes_3)
		#print("efk")
		edges=0
		for i in Graph:
			edges+=len(Graph[i])

		edges=math.ceil(edges/2)
		num_of_edges_3.append(edges)



#Graph1
fig1 = plt.figure(1)
plt.plot(np.arange(0, 10000, 2500), num_of_nodes_1, color = 'blue',label='p=0.6')
plt.plot(np.arange(0, 10000, 2500), num_of_nodes_1, 'g^')

plt.plot(np.arange(0, 10000, 2500), num_of_nodes_2, color = 'black',label='p=0.75')
plt.plot(np.arange(0, 10000, 2500), num_of_nodes_2, 'ro')

plt.plot(np.arange(0, 10000, 2500), num_of_nodes_3, color = 'red',label='p=0.9')
plt.plot(np.arange(0, 10000, 2500), num_of_nodes_3, 'b^')

plt.legend(loc='upper left')
plt.xticks(np.arange(0, 10000, 2500))
plt.xlabel('Timestamp', fontsize=14)
plt.ylabel('Number of nodes', fontsize=14)
fig1.savefig('num_of_nodes.png')


fig2 = plt.figure(2)
plt.plot(np.arange(0, 10000, 2500), num_of_edges_1, color = 'blue',label='p=0.6')
plt.plot(np.arange(0, 10000, 2500), num_of_edges_1, 'g^')

plt.plot(np.arange(0, 10000, 2500), num_of_edges_2, color = 'black',label='p=0.75')
plt.plot(np.arange(0, 10000, 2500), num_of_edges_2, 'ro')

plt.plot(np.arange(0, 10000, 2500), num_of_edges_3, color = 'red',label='p=0.9')
plt.plot(np.arange(0, 10000, 2500), num_of_edges_3, 'b^')

plt.legend(loc='upper left')
plt.xticks(np.arange(0, 10000, 2500))
plt.xlabel('Timestamp', fontsize=14)
plt.ylabel('Number of Edges', fontsize=14)
fig2.savefig('num_of_edges.png')



#for Graph 3
Graph={1:[2,3,4],2:[1],3:[1,4],4:[1,3]}
#print(Graph)

#print("p=0.8")
for t in range(0, 10000):
	print(t)
	r = randint(1,10)

	if len(Graph)==0:
		Graph=start_graph

	if r in range(1,9):
		#print("Birth")
		birth_process()

	elif r in range(9,11):
		#print("Death")
		death_process()



degree_of_nodes=[]
for node in Graph:
	degree_of_nodes.append(len(Graph[node]))

	
distinct_degrees=set(degree_of_nodes)
distinct_degrees=list(distinct_degrees)
distinct_degrees=distinct_degrees[::-1]

#print(distinct_degrees)

degree_dictionary={}

for i in distinct_degrees:
	degree_dictionary[i]=degree_of_nodes.count(i)

temp_sum=sum(degree_dictionary.values())

cummulative_value=0

for i in degree_dictionary:
	cummulative_value+=degree_dictionary[i]
	degree_dictionary[i]=cummulative_value


for i in degree_dictionary:
	degree_dictionary[i]=degree_dictionary[i]/(temp_sum)


degree_prob=list(degree_dictionary.values())

fig3 = plt.figure(3)
plt.plot(distinct_degrees, degree_prob, color = 'blue',label='p=0.8')

plt.legend(loc='upper left')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Degrees (k)', fontsize=14)
plt.ylabel('P\'(k)', fontsize=14)
fig3.savefig('log_log_graph.png')
