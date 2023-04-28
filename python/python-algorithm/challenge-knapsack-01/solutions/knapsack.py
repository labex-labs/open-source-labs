class Item(object):
    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + " v:" + str(self.value) + " w:" + str(self.weight)


class Knapsack(object):
    def fill_knapsack(self, input_items, total_weight):
        if input_items is None or total_weight is None:
            raise TypeError("input_items or total_weight cannot be None")
        if not input_items or total_weight == 0:
            return 0
        items = list([Item(label="", value=0, weight=0)] + input_items)
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                elif j >= items[i].weight:
                    T[i][j] = max(
                        items[i].value + T[i - 1][j - items[i].weight], T[i - 1][j]
                    )
                else:
                    T[i][j] = T[i - 1][j]
        results = []
        i = num_rows - 1
        j = num_cols - 1
        while T[i][j] != 0:
            if T[i - 1][j] == T[i][j]:
                i -= 1
            elif T[i][j - 1] == T[i][j]:
                j -= 1
            else:
                results.append(items[i])
                i -= 1
                j -= items[i].weight
        return results


class KnapsackTopDown(object):
    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError("input_items or total_weight cannot be None")
        if not items or not total_weight:
            return 0
        memo = {}
        result = self._fill_knapsack(items, total_weight, memo, index=0)
        return result

    def _fill_knapsack(self, items, total_weight, memo, index):
        if total_weight < 0:
            return 0
        if not total_weight or index >= len(items):
            return items[index - 1].value
        if (total_weight, len(items) - index - 1) in memo:
            return memo[(total_weight, len(items) - index - 1)] + items[index - 1].value
        results = []
        for i in range(index, len(items)):
            total_weight -= items[i].weight
            result = self._fill_knapsack(items, total_weight, memo, index=i + 1)
            total_weight += items[i].weight
            results.append(result)
        results_index = 0
        for i in range(index, len(items)):
            memo[total_weight, len(items) - i] = max(results[results_index:])
            results_index += 1
        return max(results) + (items[index - 1].value if index > 0 else 0)


class Result(object):
    def __init__(self, total_weight, item):
        self.total_weight = total_weight
        self.item = item

    def __repr__(self):
        return "w:" + str(self.total_weight) + " i:" + str(self.item)

    def __lt__(self, other):
        return self.total_weight < other.total_weight


def knapsack_top_down_alt(items, total_weight):
    if items is None or total_weight is None:
        raise TypeError("input_items or total_weight cannot be None")
    if not items or not total_weight:
        return 0
    memo = {}
    result = _knapsack_top_down_alt(items, total_weight, memo, index=0)
    curr_item = result.item
    curr_weight = curr_item.weight
    picked_items = [curr_item]
    while curr_weight > 0:
        total_weight -= curr_item.weight
        curr_item = memo[(total_weight, len(items) - len(picked_items))].item
    return result


def _knapsack_top_down_alt(items, total_weight, memo, index):
    if total_weight < 0:
        return Result(total_weight=0, item=None)
    if not total_weight or index >= len(items):
        return Result(total_weight=items[index - 1].value, item=items[index - 1])
    if (total_weight, len(items) - index - 1) in memo:
        weight = (
            memo[(total_weight, len(items) - index - 1)].total_weight
            + items[index - 1].value
        )
        return Result(total_weight=weight, item=items[index - 1])
    results = []
    for i in range(index, len(items)):
        total_weight -= items[i].weight
        result = _knapsack_top_down_alt(items, total_weight, memo, index=i + 1)
        total_weight += items[i].weight
        results.append(result)
    results_index = 0
    for i in range(index, len(items)):
        memo[(total_weight, len(items) - i)] = max(results[results_index:])
        results_index += 1
    if index == 0:
        result_item = memo[(total_weight, len(items) - 1)].item
    else:
        result_item = items[index - 1]
    weight = max(results).total_weight + (items[index - 1].value if index > 0 else 0)
    return Result(total_weight=weight, item=result_item)
