import math
graph={'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
def dijkstra(graph,start,goal):
    short_distance={}
    predecessor={}
    path=[]
    unseenNodes=graph
    infinity=math.inf
    for node in unseenNodes:
        short_distance[node]=infinity
    short_distance[start]=0
    print(short_distance)

    #  O(V)
    while unseenNodes:

        #find minimum node   ,     O(V)
        minNode=None#min be none ,ignore it
        for node in unseenNodes:
            if minNode is None:
                minNode=node
            elif short_distance[node]<short_distance[minNode]:
                minNode=node
  #Each edge visted once ,O(E)
        for neighborNode,weight in graph[minNode].items():  #min node's neighbors, each negihbor and his weight.
            print("hehe",graph[minNode])
            print("哈哈",graph[minNode].items())
            print(neighborNode,weight)
            if weight+short_distance[minNode]<short_distance[neighborNode]: #if v+weight< neighbor node
                short_distance[neighborNode]=weight+short_distance[minNode ]

                predecessor[neighborNode]=minNode  #store childeNode's previous link node
        unseenNodes.pop(minNode)
    print("s",short_distance)
    print("predecessor:",predecessor)
    currentNode=goal

    while currentNode !=start:
        try:
            path.insert(0,currentNode)
            currentNode=predecessor[currentNode]
        except KeyError:
            print("Path not reachable")  #no previous node
            break

    path.insert(0,start)
    if short_distance[goal] !=infinity:
        print('Shortest distance is '+str(short_distance[goal]))
        print('And the path is '+str(path))

source=input("Enter a source vertex:")
target=input(("Enter a target vertex:"))
dijkstra(graph,source,target)









