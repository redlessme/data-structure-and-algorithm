x= [[2,1],
    [1,4]]

y=[[2,2],
   [1,5]]

result=[[0,0],
        [0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]

for e in result:
    print(e)