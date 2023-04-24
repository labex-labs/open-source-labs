class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)
class Knapsack(object):

    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError('items or total_weight cannot be None')
        if not items or total_weight == 0:
            return 0
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [0] * (num_cols)
        for i in range(num_rows):
            for j in range(num_cols):
                if j >= items[i].weight:
                    T[j] = max(items[i].value + T[j - items[i].weight],
                               T[j])
        return T[-1]
