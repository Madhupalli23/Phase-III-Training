#Breadth First Search
def BFS(graph,root):
    visited=[root]
    q=[root]
    while len(q)!=0:
        ele=q.pop(0)
        for node in graph[ele]:
            if node not in visited:
                q.append(node)
                visited.append(node)
    return visited  

#Depth First Search
def DFS(graph,root,visited):
    s=[root]
    visited.append(root)
    while len(s)!=0:
        ele=s.pop(0)
        for node in graph[ele]:
            if node not in visited:
                DFS(graph,node,visited)
    return visited  
        
graph={
    "A" : ["B","C"],
    "B" : ["A","C","D"],
    "C" : ["A","B","E"],
    "D" : ["B","E"],
    "E" : ["C","D"]
}
r=BFS(graph,"B")
r1=DFS(graph,"E",[])
print(r)
print(r1)

