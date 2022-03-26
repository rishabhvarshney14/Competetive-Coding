class DisjointSets:
  def __init__(self, num_nodes):
    self.parent = [i for i in range(num_nodes)]
    self.rank = [0 for _ in range(num_nodes)]
      
  def findParent(self, node):
    if self.parent[node] == node:
      return node
    
    self.parent[node] = self.findParent(self.parent[node])
    
    return self.parent[node]
      
  def union(self, u, v):
    u = self.findParent(u)
    v = self.findParent(v)
    
    if self.rank[u] < self.rank[v]:
      self.parent[u] = v
    elif self.rank[u] > self.rank[v]:
      self.parent[v] = u
    else:
      self.parent[v] = u
      self.rank[u] += 1