import numpy as np
from sys import maxsize

def AssignmentBB(n,C):
  #rows
  result = [0] * n
  #rows
  for x in range(n):
    #columns
    result[x] = [0] * n
  X = SNH(n, C)
  print("Here are all solutions X with best lower bound:")
  print("X = ")
  return X

def SNH(n,C):
  X = [[0 for i in range(n)]for j in range(n)] 
  G = C.copy()
  snh = 0
  for i in range(n):
    snh += np.amin(C)
    min_coord = np.where(C == np.amin(C))
    C[:,min_coord[1][0]] = maxsize
    C[min_coord[0][0],:] = maxsize
    X[min_coord[1][0]][min_coord[0][0]] = 1
  print("UB1 = SNH(C) = ", snh)
  return X

def KnapsackDP(n, c, V, W): 
  X = [0 for i in range(len(V))]
  sackMatrix = [[0 for i in range(c + 1)]for j in range(n + 1)] 
  for j in range(n+1): 
    for i in range(c+1): 
      if j == 0 or i == 0: 
        sackMatrix[j][i] = 0
      elif W[j - 1] <= i: 
        var1 = V[j-1]+ sackMatrix[j-1][i-W[j-1]]
        var2 = sackMatrix[j-1][i]
        if(var1 > var2):
          sackMatrix[j][i] = var1
        else:
          sackMatrix[j][i] = var2
      else: 
        sackMatrix[j][i] = sackMatrix[j-1][i] 
  
  finalCost = sackMatrix[n][c]    
  #print("maximum value of sack: ",finalCost)
  var = finalCost
  w = c 
  for i in range(n, 0, -1): 
    if var == sackMatrix[i - 1][w]: 
      continue
    if var <= 0: 
      break
    else:
      X[i-1] = 1     
      var -= V[i-1] 
      w -= W[i-1] 
  return(X)


if __name__ == "__main__":
  #part 1
  C = np.matrix('6 4 2 5; 2 1 5 4; 4 2 1 3; 5 3 3 2')
  print(AssignmentBB(len(C), C))
  print()

  #part 2
  V = [20, 10, 140, 50] 
  W = [10, 20, 30, 34] 
  c = 64
  n = len(V) 
  print(KnapsackDP(n, c, V, W))