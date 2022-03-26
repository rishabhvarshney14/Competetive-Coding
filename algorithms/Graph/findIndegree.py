def findIndegree(start, end, graph):
  in_degree = [0 for _ in range(start, end+1)]
  
  for node in range(start, end+1):
    for node_itr in graph[node]:
      in_degree[node_itr] += 1
      
  return in_degree