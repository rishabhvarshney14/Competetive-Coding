def checkBipartite(node, graph, color):
  color[node] = 0
  queue = [node]
    
  while queue:
    node_temp = queue.pop(0)
        
    for node_itr in graph[node_temp]:
      if color[node_itr] == -1:
        color[node_itr] = 1 - color[node_temp]
        queue.append(node_itr)
      elif color[node_itr] == color[node_temp]:
        return False
    
  return True