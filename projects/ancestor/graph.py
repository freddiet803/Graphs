from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        our_visited_queue = set()
        our_queue = Queue()

        our_queue.enqueue(starting_vertex)
        # print(our_queue)
        while our_queue.size() > 0:
            current_node = our_queue.dequeue()
            if current_node not in our_visited_queue:
                our_visited_queue.add(current_node)

                neighbors = self.get_neighbors(current_node)
                for each_neighbor in neighbors:
                    our_queue.enqueue(each_neighbor)
                print(current_node)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        our_stack = Stack()
        our_visited_stack = set()

        our_stack.push(starting_vertex)

        while our_stack.size() > 0:
            current_node = our_stack.pop()

            if current_node not in our_visited_stack:
                our_visited_stack.add(current_node)
                neighbors = self.get_neighbors(current_node)

                for each_neighbor in neighbors:
                    our_stack.push(each_neighbor)
                print(current_node)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        """

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            print(starting_vertex)

            for each_neighbor in neighbors:
                self.dft_recursive(each_neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        our_queue = Queue()
        visited = set()

        our_queue.enqueue([starting_vertex])

        if starting_vertex == destination_vertex:
            return

        while our_queue.size() > 0:
            current_node = our_queue.dequeue()
            node = current_node[-1]

            #print(current_node, node)

            if node not in visited:
                neighbors = self.get_neighbors(node)

                for each_neighbor in neighbors:
                    new_current = list(current_node)
                    new_current.append(each_neighbor)
                    our_queue.enqueue(new_current)

                    if each_neighbor == destination_vertex:
                        return new_current
                visited.add(node)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        our_stack = Stack()
        visited = set()

        our_stack.push([starting_vertex])

        if starting_vertex == destination_vertex:
            return

        while our_stack.size() > 0:
            current_node = our_stack.pop()
            node = current_node[-1]

            if node not in visited:
                neighbors = self.get_neighbors(node)

                for each_neighbor in neighbors:
                    new_current = list(current_node)
                    new_current.append(each_neighbor)
                    our_stack.push(new_current)

                    if each_neighbor == destination_vertex:
                        return new_current
                visited.add(node)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), thePath=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        thePath = thePath + [starting_vertex]
        visited.add(starting_vertex)

        if starting_vertex == destination_vertex:
            return thePath
        if len(thePath) == 0:
            thePath.append(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)
        for each_neighbor in neighbors:
            if each_neighbor not in visited:
                new_path = self.dfs_recursive(
                    each_neighbor, destination_vertex, visited, thePath)

                if new_path:
                    return new_path
