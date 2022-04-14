#Function For Fibonacci Series

import time

def fibonacci(n):
  lst = [0,1]
  t = []
  r = n+1
  start = time.time()
  for i in range(2,r):
    start = time.time()
    lst.append(lst[i-1] +lst[i-2])
    end = time.time()
    t.append(end-start)
  j = 0
  k=1
  end = time.time()

  for i in range(1,r):
    if(k==1):
      m = "st"
    elif(k==2):
      m="nd"
    elif(k==3):
      m="rd"
    else:
      m="th"

    print(k,m,"Fibonacci No.: ",lst[j],"- Time: ",t[j-1])
    j = j+1
    k = k+1
