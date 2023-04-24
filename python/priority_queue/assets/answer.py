class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        # TODO: Implement me
        pass

    def extract_min(self):
        # TODO: Implement me
        pass

    def decrease_key(self, obj, new_key):
        # TODO: Implement me
        pass