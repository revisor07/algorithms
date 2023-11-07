def Moore(P,D):
  jobs = []
  j = 0;
  S = [];

  for i in range(len(P)) :
    jobs.append((P[i], D[i], i))

  jobs.sort(key = lambda x: x[1])
  
  for i in range(len(P)):
    S.append((j,j+jobs[i][0], jobs[i][2]))
    j += jobs[i][0]
  
  lateness = 0
  separator = False

  print("P: ", end="")
  for i in range(len(P)):
    job = S[i]   
    lateness = job[1]-jobs[i][1]
    if(lateness > 0 and not separator):
        print("| ", end="")
        separator = True
    print("J_"+str(job[2]+1) + " (" + str(job[0]) + "," + str(job[1])+"), ", end="")
  print()
  print()    


def McNaughton(P,m):
  c_max = int(max(sum(P)/m, max(P)))
  jobs = []
  for i in range(len(P)) :
    jobs.append((P[i], i))

  process = 1
  power_left = c_max

  print("P_"+str(process)+": ", end="")
  for i in range (len(P)):
    if(power_left == P[i]):
      print("J_"+str(i+1)+" ("+str(c_max-power_left)+","+str(c_max)+") ",)
    elif(power_left>P[i]):
      print("J_"+str(i+1)+" ("+str(c_max-power_left)+","+str(c_max-power_left+P[i])+"), ", end="")
      power_left = power_left-P[i]
      #print(power_left)
    elif(power_left<P[i]):
      P[i] -= power_left
      print("J_"+str(i+1)+" ("+str(c_max-power_left)+","+str(c_max)+") ")
      process += 1
      print("P_"+str(process)+": ", end="")
      power_left = c_max
      print("J_"+str(i+1)+" ("+str(c_max-power_left)+","+str(c_max-power_left+P[i])+"), ", end="")
      power_left = power_left-P[i]
  print()

def ListScheduling(P,m):
  processes = []
  for i in range(m):
    #power, index, job list
    processes.append((0, i, []))
  for i in range (len(P)):
    processes.sort(key = lambda x: x[0])
    processes[0][2].append("J_"+str(i+1)+" ("+str(processes[0][0])+", "+str(processes[0][0]+P[i])+")")
    processes[0] = (processes[0][0]+P[i], processes[0][1], processes[0][2])

  processes.sort(key = lambda x: x[1])
  for i in processes:
    print("P_"+str(i[1]+1)+": ", end="")
    for j in i[2]:
      if(j == i[2][-1]):
        print(j)
      else:
        print(str(j)+", ", end="")
  print()


def LPT(P,m):
  processes = []
  jobs = []
  for i in range(m):
    #power, index, job list
    processes.append((0, i, []))

  for i in range(len(P)):
    jobs.append((P[i], i))
  #non-increasing order because lpt
  jobs.sort(key = lambda x: x[0], reverse=True)
  for i in range (len(jobs)):
    processes.sort(key = lambda x: x[0])
    processes[0][2].append("J_"+str(jobs[i][1]+1)+" ("+str(processes[0][0])+", "+str(processes[0][0]+P[jobs[i][1]])+")")
    processes[0] = (processes[0][0]+P[jobs[i][1]], processes[0][1], processes[0][2])

  processes.sort(key = lambda x: x[1])
  for i in processes:
    print("P_"+str(i[1]+1)+": ", end="")
    for j in i[2]:
      if(j == i[2][-1]):
        print(j)
      else:
        print(str(j)+", ", end="")
  print()

def SPT(P,m):
  processes = []
  jobs = []
  for i in range(m):
    #power, index, job list
    processes.append((0, i, []))

  for i in range(len(P)):
    jobs.append((P[i], i))
  #non-decreasing order because spt
  jobs.sort(key = lambda x: x[0])
  for i in range (len(jobs)):
    processes.sort(key = lambda x: x[0])
    processes[0][2].append("J_"+str(jobs[i][1]+1)+" ("+str(processes[0][0])+", "+str(processes[0][0]+P[jobs[i][1]])+")")
    processes[0] = (processes[0][0]+P[jobs[i][1]], processes[0][1], processes[0][2])

  processes.sort(key = lambda x: x[1])
  for i in processes:
    print("P_"+str(i[1]+1)+": ", end="")
    for j in i[2]:
      if(j == i[2][-1]):
        print(j)
      else:
        print(str(j)+", ", end="")
  print()



if __name__ == "__main__":
  P = [2,4,5,2,1]
  D = [4,8,7,17,9]
  P2 = [5,5,5,5,5,5]
  P3 = [5,4,1,8,3]
  m = 5
  m2 = 3
  Moore(P,D)
  McNaughton(P2,m)
  ListScheduling(P3,m2)
  LPT(P3,m2)
  SPT(P3,m2)
