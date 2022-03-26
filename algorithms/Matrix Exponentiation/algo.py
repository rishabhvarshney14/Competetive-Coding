def matrixMultiply(A, B): 
  product = [[0, 0], [0, 0]]
  
  for i in range(2):
    for j in range(2):
      for k in range(2):
        product[i][k] += A[i][j] * B[j][k]
  
  return product
  
def expo_power(A, n):
  result = [[1, 0], [0, 1]]
  while n > 0:
    if n % 2 == 1:
      result = matrixMultiply(result, A)
    
    n //= 2 
    A = matrixMultiply(A, A)
    
  return result

def solve():
  n = int(input())
  A = [[19, 8], [6, 20]]
  result = expo_power(A, n)
  print(result[0][0])