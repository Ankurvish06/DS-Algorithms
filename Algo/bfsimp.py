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




For getting the path:
         
# graph is in adjacent list representation
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print bfs(graph, '1', '11')
