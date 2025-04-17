from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        class Node:
            def __init__(self):
                self.visited = False
                self.layer = 0

        # Creating a list with the properties of a "Node", for each vertex (or node) in "graph"
        layered_graph = [Node() for _ in range(len(graph))]

        # For each node in graph
        for index in range(len(graph)):
            # If node not visited
            if not layered_graph[index].visited:
                # Create my queue to process nodes
                queue = deque()
                # Queue the node in position "index"
                queue.append(index)
                # Visit and set the layer to 0
                layered_graph[index].visited = True
                layered_graph[index].layer = 0

                # While there are nodes left to process
                while queue:
                    # Dequeue to "current node"
                    current = queue.popleft()
                    # Visiting each neighbor of current node
                    for neighbor in graph[current]:
                        # If node not visited
                        if not layered_graph[neighbor].visited:
                            # Visit and layer it 
                            layered_graph[neighbor].visited = True
                            layered_graph[neighbor].layer = layered_graph[current].layer + 1
                            # Add to queue
                            queue.append(neighbor)
                        else:
                            if layered_graph[neighbor].layer == layered_graph[current].layer:
                                return False
        return True