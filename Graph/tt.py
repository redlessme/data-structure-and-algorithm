def dijkstra(graph,start,target):
    short_distance={}
    predecessor={}


    infinity=float("inf")
    unseenNodes=[i for i in range(len(graph_list))]


    for node in unseenNodes:
        short_distance[node]=infinity
    short_distance[start]=0
    #  O(V)

    while unseenNodes:#unseen=[0,1,2,3,4,5]

        #find minimum node   ,     O(V)
        minNode=None#min be none ,ignore it
        for node in unseenNodes:
            if minNode is None:
                minNode=node
            elif short_distance[node]<short_distance[minNode]:
                minNode=node
  #Each edge visted once ,O(E)
        #find minNode's all neghbor and his weight.

        for i in range(len(graph_list)):
            if graph_list[minNode][i]!=0 :    #min node is v, i is neighbor node
                neighborNode=i
                weight=graph_list[minNode][i]
                if short_distance[neighborNode]>weight+short_distance[minNode]:
                    short_distance[neighborNode]=weight+short_distance[minNode]
                    predecessor[neighborNode]=minNode
        unseenNodes.remove(minNode)
    print('a',short_distance)

    short_distance.pop(start)  # delete the sart point
    print('a',short_distance)


    path = []
    min = infinity
    currentNode = target
    print('cc',currentNode)
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Path not reachable")  # no previous node
            break

    path.insert(0, start)
    #short_distance[goal] != short_distance[start] and
    if  short_distance[currentNode]!=infinity:   #infinity means not reachable point,0 means itself
        print("camera "+str(i+1)+":"+str(currentNode))
        print('Distance from your location: ' + str(short_distance[currentNode]))                          #means no the path.
        print('Shortest path: ' + str(path))
    short_distance.pop(currentNode)


if __name__ == '__main__':# id is 0-6104, 6105个

    graph_list = [[0 for x in range(6)] for x in range(6)]
    n=5
    with open("test_edges.txt") as f:
        content = f.readlines()
    edgesList = []
    for x in content:
        a=x.strip()
        eachRoad=a.split()
        eachRoad[0], eachRoad[1], eachRoad[2]= int(eachRoad[0]), int(eachRoad[1]), float(eachRoad[2])
        edgesList.append(eachRoad)
    print("edge",edgesList)
    # print("e",len(edgesList))
    # print(alist)
    for i in range(len(edgesList)):
        v1=edgesList[i][0]
        v2=edgesList[i][1]
        if len(edgesList[i])==4:
            if edgesList[i][3]=="TOLL":
                distance=0
        else:
            distance=edgesList[i][2]
        graph_list[v1][v2]=distance
        graph_list[v2][v1]=distance#beacuse it is a undirected graph


    source = input("Enter a source vertex:")
    #k=int(input("Enter k:"))
    target = input(("Enter a target vertex:"))
    dijkstra(graph_list, int(source),int(target))

