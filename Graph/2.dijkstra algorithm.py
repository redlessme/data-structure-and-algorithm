from heapq import *

def dijkstra(graph,start,target):
    short_distance={}
    predecessor={}


    infinity=float("inf")
    unseenNodes=[i for i in range(len(graph_list[0]))]

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
    currentNode=target

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

    graph_list =[[0, 10, 5, 0, 0],
                [10, 0,  3, 1, 0],
                [0, 0, 0, 0, 0],
                [5, 3, 0, 9, 2],
                [0, 1, 9, 0, 6],
                [0, 0, 2, 6, 0]]

    source = input("Enter a source vertex:")

    target = input(("Enter a target vertex:"))
    dijkstra(graph_list, int(source),int(target))

