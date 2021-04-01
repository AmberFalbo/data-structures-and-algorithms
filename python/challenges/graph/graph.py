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
        if vertex not in self._adjacency_list:
            raise KeyError(f'{vertex} not a vertex in {self}')

    def size(self):
        return len(self._adjacency_list)

    def breadth_first(self, node):
        pass

    def get_edge(self, node):
        pass

