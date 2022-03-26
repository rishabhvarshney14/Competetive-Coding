def dfs_helper(node, stack, graph, vis):
  vis[node] = True
  
  for node_itr in graph[node]:
    if vis[node_itr] != True:
      dfs_helper(node_itr, stack, graph, vis)
  
  stack.append(node)
            
def transpose(n, graph):
  new_edges = [[] for _ in range(n)]
    
  for node in range(n):
    for node_itr in graph[node]:
      new_edges[node_itr].append(node)
    
  return new_edges

def revDFS(node, graph, vis, components):
  vis[node] = True
  components.append(node)
    
  for node_itr in graph[node]:
    if vis[node_itr] == False:
      revDFS(node_itr, graph, vis, components)

def kosarajuAlgo(n, graph):
  stack = []
  vis = [False for _ in range(n)]
    
  for node in range(n):
    if vis[node]!= True:
      dfs_helper(node, stack, graph, vis)
    
  transpose_edges = transpose(n, graph)
  vis = [False for _ in range(n)]
  components = []
  while stack:
    node = stack.pop()
    if vis[node] == False:
      temp = []
      revDFS(node, transpose_edges, vis, temp)
      components.append(temp)
     
  return components