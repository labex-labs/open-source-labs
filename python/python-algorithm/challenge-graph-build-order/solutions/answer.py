from collections import deque


class Dependency(object):
    def __init__(self, node_key_before, node_key_after):
        self.node_key_before = node_key_before
        self.node_key_after = node_key_after


from enum import Enum


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


class BuildOrder(object):
    def __init__(self, dependencies):
        self.dependencies = dependencies
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        for dependency in self.dependencies:
            self.graph.add_edge(dependency.node_key_before, dependency.node_key_after)

    def _find_start_nodes(self, processed_nodes):
        nodes_to_process = {}
        for key, node in self.graph.nodes.items():
            if node.incoming_edges == 0 and key not in processed_nodes:
                nodes_to_process[key] = node
        return nodes_to_process

    def _process_nodes(self, nodes_to_process, processed_nodes):
        for node in nodes_to_process.values():
            # We'll need to iterate on copies since we'll need
            # to change the dictionaries during iteration with
            # the remove_neighbor call
            for adj_node in list(node.adj_nodes.values()):
                node.remove_neighbor(adj_node)
            processed_nodes[node.key] = node
        nodes_to_process = {}

    def find_build_order(self):
        result = []
        nodes_to_process = {}
        processed_nodes = {}
        while len(result) != len(self.graph.nodes):
            nodes_to_process = self._find_start_nodes(processed_nodes)
            if not nodes_to_process:
                return None
            result.extend(nodes_to_process.values())
            self._process_nodes(nodes_to_process, processed_nodes)
        return result
