graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

   def dfs(s,d):
    def dfs_helper(s,d):
        if s == d:
            return True
        if  s in visited :
            return False
        visited.add(s)
        for c in graph[s]:
            dfs_helper(c,d)
        return False
    visited = set()
    return dfs_helper(s,d) 
dfs('A','E') ---- True
dfs('A','M') ---- False
