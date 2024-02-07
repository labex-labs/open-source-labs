import sys
from enum import Enum


class PriorityQueueNode(object):
    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ": " + str(self.key)


class PriorityQueue(object):
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        return self.array[-1]

    def extract_min(self):
        if not self.array:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.array):
            if node.key < minimum:
                minimum = node.key
                minimum_index = index
        return self.array.pop(minimum_index)

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj is obj:
                node.key = new_key
                return node
        return None


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
        if neighbor is None or weight is None:
            raise TypeError("neighbor or weight cannot be None")
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError("neighbor cannot be None")
        if neighbor.key not in self.adj_nodes:
            raise KeyError("neighbor not found")
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:
    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, key):
        if key is None:
            raise TypeError("key cannot be None")
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError("Invalid key")
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, src_key, dst_key, weight=0):
        if src_key is None or dst_key is None:
            raise TypeError("key cannot be None")
        self.add_edge(src_key, dst_key, weight)
        self.add_edge(dst_key, src_key, weight)


class ShortestPath(object):
    def __init__(self, graph):
        # TODO: Implement me
        pass

    def find_shortest_path(self, start_node_key, end_node_key):
        # TODO: Implement me
        pass
