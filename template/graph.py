import sys
input = sys.stdin.readline

def int_1():
  return int(input())

def int_k():
  return map(int, input().split())

def int_l():
  return list(int_k())

def getGraph(start, end, loop):
  graph = {i: [] for i in range(start, end+1)}
  
  for _ in range(loop):
    u, v = int_k()
    graph[u].append(v)
    graph[v].append(u)
  
  return graph

def solve():
  pass

for _ in range(int_1()):
  solve()
