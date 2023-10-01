import sys, os.path as osp

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from modules import *
from collections import deque
from graph_adjacency_list import GraphAdjList
from collections import defaultdict

"""
Given a 7x7 grid matrix,index starting from 0 to 6, Robot is given the knowledge of Grid Occupancy Mapping, current location, and the destination as illustrated below:
Current robot's location is at (1, 3), destination is at (6, 2), and the occupied cells are (3,2),(3,3),(3,4),(4,2),(4,3),(4,4).
Write a solution class to search for a navigable path from current location to the destination, 
and validate your solution against the illustrated sample in the main() function.

Note that the robot can only move to adjacent cells either vertically or horizontally but not diagonally!
"""
from collections import deque
class robot:
	def __init__(self, grid_size, occupied_cells, current_location, destination) -> None:
		self.grid_size = grid_size
		self.occupied_cells = occupied_cells
		self.current_location = current_location
		self.destination = destination
	def isValidLocation(self, location)-> bool:
		x = location[0]; y = location[1]
		return True if (0 <= x <= self.grid_size[0]- 1) and (0 <= y <= self.grid_size[1]-1) and \
													(location not in occupied_cells) else False
	def find_path(self)-> []: # return list of tuples 
		visited = set[tuple]() # 
		# queue = deque([(self.current_location, [])]) # tuple and a empty list
		Queue = deque([(self.current_location, [])]) # list with (tuple and list), feed the start point
		cnt = 0
		while Queue: # pop 
			q = Queue.popleft() # list of (tuple and list of tuples) 
			current = q[0]
			path = q[1] 
			# print("path before",path)
			# print(type(path))
			if self.isValidLocation(current) == False: # invalid location, discard.
				continue
			# Valid location 
			if current in visited: # visited location already, traverse next
				continue
			visited.add(current) # add into visited
			# print("Queue 1",Queue)

			# path.append(current) # !!! This is wrong 
			path = path + [current] # !!!!!This is very important shit 
			# print("path",path)
			# print("Queue 2",Queue)
			if current == self.destination: # check if current location is destination 
				return path
			x, y = q[0]
			left= [(x - 1 , y), path]
			right =[(x + 1 , y), path]
			up = [(x, y + 1), path]
			down = [(x, y - 1), path]
			# left= [(q[0][0] - 1 , q[0][1]), path]
			# right =[(q[0][0] + 1 , q[0][1]), path]
			# up = [(q[0][0], q[0][1] + 1), path]
			# down = [(q[0][0], q[0][1]- 1), path]
			# print("left",left)
			# print("right",right)
			# print("up",up)
			# print("down",down)
			# print("Queue before append left",Queue)
			if self.isValidLocation(left[0]):
				Queue.append(left) #append tuple(move) and list(path + [current])
			# print("Queue before append right",Queue)
			if self.isValidLocation(right[0]):
				Queue.append(right) #append tuple(move) and list(path + [current])
			# print("Queue before append up",Queue)
			if self.isValidLocation(up[0]):
				Queue.append(up) #append tuple(move) and list(path + [current])
			# print("Queue before append down",Queue)
			if self.isValidLocation(down[0]):
				Queue.append(down) #append tuple(move) and list(path + [current])
			# Queue.append(left)
			# Queue.append(right)
			# Queue.append(up)
			# Queue.append(down)
			# print(Queue)
			# print("cnt=%d"%(cnt))
			# cnt+=1
			# if cnt == 3:
			# 	return []
		print("not found")
		return []

if __name__ == '__main__':
	# for i 
	grid_size = (7, 7)
	occupied_cells = [(3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)]
	current_location = (1, 3)
	destination = (6, 2)
	r = robot(grid_size, occupied_cells, current_location, destination)

	path = r.find_path()
	if path:
		print("Path found:")
		for step in path:
			print(step)
	else:
		print("No path found!")
	# Queue = deque([[self.current_location, [     ]]]) # list with (tuple and list), feed the start point
	# Queue=deque([[current_location,      [(2,3)]]]) # list with (tuple and list), feed the start point
	# Queue.append([(3,3),[(4,3),(5,3)]])
	# q1 = Queue.popleft() 
	# print(q1[0],q1[1]) # tuple
# Queue = deque([(self.current_location, [])]) # list with (tuple and list), feed the start point
	# Q = deque([((1, 3),                [])])
	# # Q = deque([[(0, 3), [(1, 3)]], [(2, 3), [(1, 3)]], [(1, 4), [(1, 3)]], [(1, 2), [(1, 3)]]])
	# Q.append([(0, 3), [(1, 4)]])
	# Q.append([(2, 3), [(1, 5)]])
	# print("initQ", Q)
	# current,path = Q.popleft()
	# print("after pop Q", Q)
	# path.append(current)
	# print("after append Q", Q)
	# current
	# while Q:
	# 	current,path = Q.popleft()
		# print(type(element[0])); # print(type(element[1])); # print(type(element[1][0])); # print(type(element[1][0][0]));
	# print(path)
	# t,l = Q.popleft()
	# print(l)
	# t2= (9,9)
	# l.append(t2)
	# print(l)
	# t,l = Q.popleft()
	# print(l)

