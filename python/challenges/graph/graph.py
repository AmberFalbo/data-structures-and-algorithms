from ..stacks_and_queues.stacks_and_queues import Queue

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self):
        self._adjacency_list = {}
    
    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError('The start vertex is not in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('The end vertex not in graph')
        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_node(self):
        vetices = self._adjacency_list.keys()
        return vetices

    def get_neighbor(self, vertex):
        edges = []
        if vertex not in self._adjacency_list:
            raise KeyError(f'{vertex} not a vertex in {self}')
        for key_pair in self._adjacency_list[vertex]:
            edges.append((key_pair.vertex, key_pair.weight))
        return edges


    def size(self):
        return len(self._adjacency_list)

    # def breadth_first(self, node):
    #     queue = Queue()
    #     values = []
    #     queue.enqueue(node)

    #     while queue.front != None:
    #         node = queue.dequeue()
    #         new_list.append(node.value)
    #         if node.neighbor != None:
    #             q.enqueue(node.left)
    #     return new_list  



    def get_edge(self, node):
        pass

