import heapq
from collections import defaultdict
edgesList = []
with open('edges.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
        line = line.split(' ')
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[2] = float(line[2])
        if len(line) == 3: #ignore toll road
            edgesList.append(line)
    print(len(edgesList))

class Graph:
    def __init__(self, n):
        self.nodes = set(range(n))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, vertex1, vertex2, distance):
        self.edges[vertex1].append(vertex2)# {2: [2, 5], 1: [2]})
        self.edges[vertex2].append(vertex1)  #beacuse it is undirected graph
        self.distances[vertex1, vertex2] = distance #{(1, 2): 8}
        self.distances[vertex2, vertex1] = distance

def dijkstra(graph, start, minTargetPoint):

    pre={}
    infinity=float("inf")

    short_distance={}

    with open("vertices.txt") as e:
        line=e.readlines()

        cameraList=[]
        for ele in line:
            ele=ele.strip()
            ele=int(ele)
            cameraList.append(ele)

    for node in range(6105):#O(V)
            short_distance[node]=infinity
    short_distance[start]=0
    minHeap = [(0, start)]

    while  minHeap: # O(V)
        if start in cameraList:   #if start point has red light camera, path is not reachable
            print("Oops! Cannot help, Alice!!! Smile for the camera!")
            return

        current_weight, min_node = heapq.heappop(minHeap)   #get min node O(1)
                                                            # and remove min node and heapify is O(logv)

        for neighborNode in graph.edges[min_node]:# v are minnode's neighbor  # becase visit all edges, so it's O(E)

            weight=graph.distances[min_node,neighborNode] + short_distance[min_node]


            if short_distance[neighborNode] > weight :
                short_distance[neighborNode] = weight
                heapq.heappush(minHeap, (short_distance[neighborNode], neighborNode))# o(logv)
                pre[neighborNode] = min_node

            if neighborNode in cameraList and (short_distance[neighborNode],neighborNode) in minHeap:
                heapq.heappop(minHeap) #O(logv)

    for i in range(k):
        path = []
        min = infinity
        for item,weight in short_distance.items():

            if weight<min and item in cameraList:
                min=weight
                minTargetPoint=item

        currentNode = minTargetPoint
        #
        while currentNode != start:
            try:
                path.insert(0, currentNode)
                currentNode = pre[currentNode]
            except KeyError:
                print("Oops! You’re stuck here Alice!")  # no previous node
                return

        path.insert(0, start)
        # short_distance[goal] != short_distance[start] and

        paths=''
        for ele in path:
            paths+=str(ele)
            paths+=" --> "
        paths=paths[0:-4]

        # if min target point not in the dict, return ,means no other cameras!

        try:#k <camera
            short_distance[minTargetPoint]
        except KeyError:
            return
        if short_distance[minTargetPoint] != infinity:  # infinity means not reachable point,0 means itself
            print("\ncamera " + str(i+1)+":" + str(minTargetPoint)+'  Distance from your location: ' + str(short_distance[minTargetPoint]))
            print('Shortest path: ' + paths)
        short_distance.pop(minTargetPoint)

if __name__ == '__main__':
    graph = Graph(6105)
    for i in range(len(edgesList)):
        graph.add_edge(edgesList[i][0], edgesList[i][1], edgesList[i][2])
    soure=int(input("Enter a source vertex:"))
    k=int(input("Enter k:"))
    dijkstra(graph,soure,k)
