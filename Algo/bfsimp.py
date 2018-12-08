graph = {'A': ['B','Y','D', 'E',],
         'B': ['F','F'],
         'C': ['F'],
         'D': [],
         'E': ['F','G'],
         'F': ['F','A'],
         'G': ['E','K'],
         'K': ['M','L']
         }
         
from collections import deque

def bfs(graph, start, end):
    """Return True if there is a path from start to end in graph, False if
    not. graph must be a dictionary mapping a node to a collection of its
    neighbours.
    """
    if start == end:
        return True
    queue = deque([start])
    visited = set(queue)
    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, ()):
            if neighbour not in visited:
                if neighbour == end:
                    return True
                queue.append(neighbour)
                visited.add(neighbour)
    return False
