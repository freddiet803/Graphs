'''
linked list: network where nodes can have just 
one connection

BST: network where nodes can have a left and right

graph: 
node aka vertices (one vertex, many vertices)
connections aka edges

in a graph we can have a node with no connections
contrast with ll, node with no edges isnt in ll




network: 

LL traversal: while loop starting from head

BST traversal: 
search left and right 
bst_traversal:
    print node
    if node == none
        return
    bst_traversal(left)
    bst_traversal(right)


want to generalize traversal
graph traversal will work for ll and bst

acyclic vs cyclic:
    can we go in a circle or not? hit a node more than once?
weighted vs unweighted:
    labels on edges, numbers on the edge or connection - ex a map with distance

sparse vs dense:
    do we have a lot of nodes or not?
directed vs undirected:
    one way street vs two way streets

why traversals are important to other algorithms
graph applications
    if you can think of problem as graph, then you can use this concept


'''


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def dft_traverse(node):  # node or self? self would be the class
    our_visited_set = set()
    our_stack = Stack()

    our_stack.push(node)

    while our_stack.size() > 0:
        current_node = our_stack.pop()
        if current_node not in our_visited_set:
            our_visited_set.add(current_node)
            neighbors = current_node.neighbors

            for each_neighbor in neighbors:
                our_stack.push(each_neighbor)

            '''if len(current_node.neighbors) > 0:
                for each_neighbor in current_node.neighbors:
                    our_stack.push(each_neighbor)'''


def bft_traverse(node):
    our_visited_set = set()
    our_queue = Queue()

    our_queue.enqueue(node)

    while our_queue.size() > 0:
        current_node = our_queue.dequeue()
        if current_node not in our_visited_set:
            our_visited_set.add(current_node)
            neighbors = current_node.neighbors

            for each_neighbor in neighbors:
                our_queue.enqueue(each_neighbor)


node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node5 = GraphNode(5)

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node1.neighbors.append(node4)

node5.neighbors.append(node4)
node3.neighbors.append(node4)

node4.neighbors.append(node1)
