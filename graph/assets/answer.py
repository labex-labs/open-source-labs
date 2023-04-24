from enum import Enum  # Python 2 users: Run pip install enum34


class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        # TODO: Implement me
        pass

    def remove_neighbor(self, neighbor):
        # TODO: Implement me
        pass


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, id):
        # TODO: Implement me
        pass

    def add_edge(self, source, dest, weight=0):
        # TODO: Implement me
        pass

    def add_undirected_edge(self, source, dest, weight=0):
        # TODO: Implement me
        pass