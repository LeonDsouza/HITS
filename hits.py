def incoming(transpose):
	count_incoming = [0] * 5
	
	for _ in range(5):
		for __ in range(5):
			if(transpose[_][__] == 1):
				count_incoming[_] = count_incoming[_] + 1
	return count_incoming
			

def outgoing(Adjacency):
	count_outgoing = [0] * 5
	
	for _ in range(5):
		for __ in range(5):
			if(Adjacency[_][__] == 1):
				count_outgoing[_] = count_outgoing[_] + 1
	return count_outgoing

def normalize(a_vector):		
	r_square = math.sqrt(sum(map(lambda x:x*x,a_vector)))
	for _ in range(5):
		a_vector[_] /= r_square
	return a_vector


import numpy as np
import math


Adjacency = np.array([[0,0,0,1,1], [0,0,0,1,0], [0,0,0,1,1], [1,0,0,0,0], [0,0,0,0,0]])
print(Adjacency)
transpose = np.transpose(Adjacency)
print(transpose)
kmax = 20
for i in range(5):
	for j in range(5):
		print(Adjacency[i][j])
a_vector = incoming(transpose)
print(a_vector)

h_vector = outgoing(Adjacency)
print(h_vector)





print(normalize(a_vector))
print(normalize(h_vector))








