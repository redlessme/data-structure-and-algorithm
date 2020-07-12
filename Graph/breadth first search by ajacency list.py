from collections import deque
graph = {'A': ['B', 'C'],
         'B': ['A', 'E', 'F'],
         'C': ['A', 'D'],
         'D': ['C'],
         'E': ['B', 'F', 'G', 'H'],
         'F': ['B', 'G', 'H', 'E'],
         'G': ['E', 'F', 'H'],
         'H': ['E', 'F', 'G']}


# visits all the nodes of a graph (connected component) using BFS


def bfs(graph,source_node):
    q=deque()
    q.append(source_node)
    visited=[source_node]
    while q:
        node=q.popleft()
        q
        neighbours=graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                q.append(neighbour)
                visited.append(neighbour)
                print(neighbour)


# def bfs_connected_component(graph, source_node):
#     queque=[source_node]
#     distance={}
#     distance[source_node]=0
#     visited=[source_node]
#     while queque:
#         node=queque.pop(0)  #source node
#         neighbours=graph[node]  #neighbor vertex
#         for neighbour in neighbours:
#             if neighbour not in visited:
#                 queque.append(neighbour)  #discovered
#                 distance[neighbour]=distance[node]+1  #
#                 visited.append(neighbour)
#                 print(neighbour+"-->"+str(distance[neighbour]))
bfs(graph,"A")




# bfs_connected_component(graph, 'A')