'''
bredth first search algorithm  is a graph traversing technique, where you select a random node (source of root node) &
start traversing the graph layer-wise in such a way that all the nodes & their respective childern nodes are visted and explored
'''
#sample graph implmented as a dictionary
graph ={'A':['B', 'C' ,'E'],
'B':['A','D','E'],
'C':['A', 'F', 'G'],
'D':['B'],
'E':['A', 'B', 'D'],
'F':['C'],
'G':['C']}


#VISTIS ALL THE NODES OF A GRAPH (CONNECTED COMPONENT)
def bfs_connected_component(graph, start):
    #keeping track of all visted nodes 
    explored = []
    #keep track of nodes to be checked
    queue = [start]
    #keep looping until there are nodes still to be seen
    while queue:
        #pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            print(node)


            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
bfs_connected_component(graph, 'A')#returns ['A', 'B', 'C', 'D', 'E','F', 'G'] 

#%%
#sample graph implmented as a dictionary
graph ={'A':['B', 'C' ,'E'],
'B':['A','D','E'],
'C':['A', 'F', 'G'],
'D':['B'],
'E':['A', 'B', 'D'],
'F':['C'],
'G':['C']}
# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                print(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 
bfs_shortest_path(graph, 'G', 'D')  # returns ['G', 'C', 'A', 'B', 'D']


# %%
