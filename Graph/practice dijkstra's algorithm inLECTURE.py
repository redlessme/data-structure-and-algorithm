graph={'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
def dijkstra(graph,source_vertex):
    discoverd=[]
    discoverd.append({source_vertex:0})
    # discoverd={'a':1,'b':2}

    print(discoverd)

    while discoverd:
        min=0
        #find minimum
        for nodes in discoverd:
            print(nodes)
            #{a,0}# print(key,item)
            for key in nodes.items():
                if discoverd[key]>min:
                    min=key












dijkstra(graph,'a')