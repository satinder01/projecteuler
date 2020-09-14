#!/Users/satinderjitsingh/anaconda3/bin/python
'''
Lattice paths

Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
00---01---02
|    |     |
|    |     |
10---11---12
|    |     |
|    |     |
20---21---22
'''


#create 20x20 graph
graph20x20 = {}

grid_dimension = 20

grid_range = grid_dimension + 1

fre={}

for row in range (grid_range):
  for col in range (grid_range):
    current_node ='r'+str(row)+'c'+str(col)
    fre[current_node]=0

  
for row in range (grid_range):
  for col in range (grid_range):
    #add edges to right nodes
    current_node ='r'+str(row)+'c'+str(col)
    right_node = 'r'+str(row)+'c'+str(col+1)
    bottom_node = 'r'+str(row+1)+'c'+str(col)
    if(row==(grid_dimension) and col==(grid_dimension)):
      graph20x20[current_node]=[]
    elif(col==(grid_dimension)):
      graph20x20[current_node]=[bottom_node]
      fre[bottom_node] = fre[bottom_node] + 1
    elif(row==(grid_dimension)):
      graph20x20[current_node]=[right_node]
      fre[right_node] = fre[right_node] + 1
    else:
      graph20x20[current_node] = [right_node, bottom_node]
      fre[right_node] = fre[right_node] + 1
      fre[bottom_node] = fre[bottom_node] + 1

#print(fre)

# function to make topological sorting 
def topological_sorting(fre, graph):
  q=[] 

  # insert all vertices which 
  # don't have any parent. 
  for i in graph:
    if not fre[i]:
      q.append(i); 

  l=[]

  # using kahn's algorithm 
  # for topological sorting 
  while q:
    u = q.pop(0); 
    ## insert front element of queue to vector 
    l.append(u); 
    ## go through all it's childs 
    for child in graph[u]:
      fre[child]=fre[child]-1
      ## whenever the freqency is zero then add 
      ## this vertex to queue. 
      if not fre[child]:
        q.append(child); 
  #print("l...",l)
  return l; 
 
 
## Function that returns the number of paths 
##int numberofPaths(int source, int destination, int n, int fre[]) 
def numberofPaths(source, destination, graph, fre):
## make topological sorting 
  s = topological_sorting(fre, graph); 
  ## to store required answer. 
  dp={}
  for row in range (grid_range):
    for col in range (grid_range):
      current_node ='r'+str(row)+'c'+str(col)
      dp[current_node]=0

    ## answer from destination 
    ## to destination is 1. 
  dp[destination] = 1; 
  
  ## traverse in reverse order 
  for i in reversed(s):
    #print("i...", i)
    for j in graph[i]:
      #print("j...", j)
      dp[i] = dp[i] + dp[j]
      #print("dp[i]....", dp[i])
      #print("dp[j]....", dp[j])
  
  return dp[source]
 
print(numberofPaths('r0c0', 'r20c20', graph20x20, fre))
#numberofPaths('r0c0', 'r2c2', graph20x20, fre)
