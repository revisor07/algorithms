from sys import maxsize
  
inf = maxsize

def Floyd(G): 
  size = len(G)
  init = False
  A = G.copy()
  printStep(A, size, 0, init) 
  init = True
  for k in range(size): 
    for i in range(size): 
      for j in range(size): 
        A[i][j] = min(A[i][j], A[i][k]+ A[k][j])     
    printStep(A, size, k, init)   

def printStep(A, size, vertex, init): 
  print()
  if(init):
    print("Phase ", vertex+1," (use Vertex ", vertex, ")")
  else:
    print("Initialization:")

  for i in range(size): 
    for j in range(size): 
      if(A[i][j] == inf): 
        print ("inf", end=" ") 
      else: 
        print (A[i][j], end=" ")
      if j == size-1: 
        print ("")


def CVRP(A,S):
  n = len(S)
  all_vertices = []
  for i in range(n):
    all_vertices.append(i)
  visited=[]
  temp = []
  k = 0
  total = 0
  heu_count = 0
  savings = [[0 for i in range(n)]for j in range(n)] 
  for i in range(1,n):
    for j in range(2+k,n):
      old = 2*S[0][i]+2*S[0][j]
      new = S[i][j]+S[0][i]+S[0][j]

      if(A[i][j] > 0) :
        if(new < old):
          savings[i][j] = old-new
          temp.append((i,j,old-new, new))
    k+=1

  print("Routes")
  for x in temp:
    if (not x[0] in visited or not x[1] in visited):
      heu_count+=x[3]
      print("O - ",chr(65+x[0]-1)," - ",chr(65+x[1]-1)," - O (Length:",x[3],")")
      
      visited.append(x[0])
      visited.append(x[1])
  for x in all_vertices:
    if(not x in visited):
      if(x != 0):
        print("O - ", chr(65+x-1)," - O (Length:", S[0][x]*2,")")
        heu_count += S[0][x]*2     

  for x in all_vertices:
    total += S[0][x]*2



  print()
  print("The matrix with the Savings-values:")
  print()
  for i in range(1,n): 
    for j in range(1,n):       
      print(savings[i][j], end="")
    print()
  print()
  print("Total length of roundtrips: ",total)
  print("Total length of Savings’s Heuristic: ", heu_count)





if __name__ == "__main__":
  A=[[0, 3, 2, 4, 2, 3],
    [3, 0, 5, 0, 0, 2],
    [2, 5, 0, 6, 0, 0],
    [4, 0, 6, 0 ,4 ,0],
    [2, 0, 0, 4, 0, 4],
    [3, 2, 0, 0, 4, 0]]

  G = [[0,3,inf,6,inf], 
      [inf,0,inf,2,4],
      [3,inf,0,inf,inf], 
      [inf, inf, 1, 0, 1], 
      [inf, inf, inf, inf, 0] 
    ] 

  S = [[0,3,2,4,2,3], 
       [0,0,5,7,5,2],
       [0,0,0,6,4,5],
       [0,0,0,0,4,7],
       [0,0,0,0,0,4], 
       [0,0,0,0,0,0] 
    ]

  #Floyd(G); 
  CVRP(A,S)

