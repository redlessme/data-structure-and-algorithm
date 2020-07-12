inf=float("inf")

def dijkstra(graph,n):
    discoverd=0*n
    flag=[False]*n #visted?
    flag[0]=True
    pre=[0]*n
    k=0

    for i in range(n):
        discoverd[i]=graph[k][i]

    for j in range(n-1):#while not empty
        min=inf
        for i in range(n):
            if discoverd[i]<min and not flag[i]:
                min=discoverd[i]
                k=i
        if k==0:
            return
        flag[k]=True
        for i in range(n):
            if discoverd[i]>