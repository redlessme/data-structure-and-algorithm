graph = {'A': [{'B':0}, {'C':0}],
         'B': [{'A':0}, {'E',0}, {'F':0}],
         'C': [{'A':0}, {'D':0}],
         'D': [{'C':0}],
         'E': [{'B':0}, {'F':0}, {'G':0}, {'H':0}],
         'F': [{'B':0}, {'G':0}, {'H':0}, {'E':0}],
         'G': [{'E':0}, {'F':0}, {'H':0}],
         'H': [{'E':0}, {'F':0}, {'G':0}]}


def BFS(graph,source_node):
    discoved = []
    discoved.append(source_node)
    visted=[source_node]
    # distance={}
    # distance[source_node]=0
    while discoved: # if discovered is not empty
        get_vertex =discoved.pop()
        neighbors=graph[get_vertex]
        for neighbor in neighbors:
            if neighbor not in visted:
                distance[neighbor]=distance[get_vertex]+1
                discoved.append(neighbor)
                visted.append(neighbor)
                print(neighbor+"--->"+str(distance[neighbor]))

BFS(graph, "A")


# def BFS(graph,source_node):
#     discovered=[source_node]
#     distance={}
#     distance[source_node]=0
#     visited=[source_node]
#     while discovered:
#         vertex=discovered.pop()
#         neighbors=graph[vertex]
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 discovered.append(neighbor)
#                 distance[neighbor]=distance[vertex]+1
#                 visited.append(neighbor)
#                 print(neighbor+"--->"+str(distance[neighbor]))
