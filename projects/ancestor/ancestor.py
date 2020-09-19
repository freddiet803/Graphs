'''help'''


from util import Stack, Queue  # imports


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That value doesnt exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("That Value doesnt exist")


def earliest_ancestor(ancestors, starting_node):

    our_graph = Graph()
    visited = set()
    q = Queue()

    for ancestor in ancestors:
        our_graph.add_vertex(ancestor[0])
        our_graph.add_vertex(ancestor[1])
        our_graph.add_edge(ancestor[1], ancestor[0])

    '''for each_thing in our_graph.vertices:
        print(each_thing, ':', our_graph.vertices[each_thing])'''

    q.enqueue(starting_node)

    earliest = []

    while q.size() > 0:
        current_node = q.dequeue()

        if current_node not in visited:
            visited.add(current_node)

        neighbors = our_graph.get_neighbors(current_node)
        for each_neighbor in neighbors:
            q.enqueue(each_neighbor)
            earliest.append(each_neighbor)

    print(our_graph.vertices)

    if earliest:
        return earliest[-1]
    else:
        return -1


our_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (
    5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(our_ancestors, 6))
