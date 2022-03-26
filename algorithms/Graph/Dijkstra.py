import heapq

def dijkstraAlgo(source, graph, n):
  min_heap = []
  distance = [float('inf')] * (n+1)
  distance[source] = 0
  
  heapq.heappush(min_heap, [source, 0])
  
  while min_heap:
    node, weight = heapq.heappop(min_heap)
    
    for node_itr, weight_itr in graph[node]:
      if weight_itr + weight < distance[node_itr]:
        distance[node_itr] = weight_itr + weight
        heapq.heappush(min_heap, [node_itr, distance[node_itr]])
    
  return distance