# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine which items to select to maximize total value.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we replace the items once they are placed in the knapsack?
  - No, this is the 0/1 knapsack problem
- Can we split an item?
  - No
- Can we get an input item with weight of 0 or value of 0?
  - No
- Can we assume the inputs are valid?
  - No
- Are the inputs in sorted order by val/weight?
  - Yes, if not we'd need to sort them first
- Can we assume this fits memory?
  - Yes

## Test Cases

- items or total weight is None -> Exception
- items or total weight is 0 -> 0
- General case

```txt
total_weight = 8
items
  v | w
  0 | 0
a 2 | 2
b 4 | 2
c 6 | 4
d 9 | 5

max value = 13
items
  v | w
b 4 | 2
d 9 | 5
```

## Algorithm

We'll use bottom up dynamic programming to build a table.

The solution for the top down approach is also provided below.

```txt
v = value
w = weight

               j
    -------------------------------------------------
    | v | w || 0 | 1 | 2 | 3 | 4 | 5 | 6  | 7  | 8  |
    -------------------------------------------------
    | 0 | 0 || 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  |
i a | 2 | 2 || 0 | 0 | 2 | 2 | 2 | 2 | 2  | 2  | 2  |
  b | 4 | 2 || 0 | 0 | 4 | 4 | 6 | 6 | 6  | 6  | 6  |
  c | 6 | 4 || 0 | 0 | 4 | 4 | 6 | 6 | 10 | 10 | 12 |
  d | 9 | 5 || 0 | 0 | 4 | 4 | 6 | 9 | 10 | 13 | 13 |
    -------------------------------------------------

i = row
j = col

if j >= item[i].weight:
    T[i][j] = max(item[i].value + T[i - 1][j - item[i].weight],
                  T[i - 1][j])
else:
    T[i][j] = T[i - 1][j]
```

Complexity:

- Time: O(n \* w), where n is the number of items and w is the total weight
- Space: O(n \* w), where n is the number of items and w is the total weight

## Code

### Item Class

```python
class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)
```

### Knapsack Bottom Up

```python
class Knapsack(object):

    def fill_knapsack(self, input_items, total_weight):
        if input_items is None or total_weight is None:
            raise TypeError('input_items or total_weight cannot be None')
        if not input_items or total_weight == 0:
            return 0
        items = list([Item(label='', value=0, weight=0)] + input_items)
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                elif j >= items[i].weight:
                    T[i][j] = max(items[i].value + T[i - 1][j - items[i].weight],
                                  T[i - 1][j])
                else:
                    T[i][j] = T[i - 1][j]
        results = []
        i = num_rows - 1
        j = num_cols - 1
        while T[i][j] != 0:
            if T[i - 1][j] ==  T[i][j]:
                i -= 1
            elif T[i][j - 1] ==  T[i][j]:
                j -= 1
            else:
                results.append(items[i])
                i -= 1
                j -= items[i].weight
        return results
```

### Knapsack Top Down

```python
class KnapsackTopDown(object):

    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError('input_items or total_weight cannot be None')
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
```

### Knapsack Top Down Alternate

```python
class Result(object):

    def __init__(self, total_weight, item):
        self.total_weight = total_weight
        self.item = item

    def __repr__(self):
        return 'w:' + str(self.total_weight) + ' i:' + str(self.item)

    def __lt__(self, other):
        return self.total_weight < other.total_weight


def knapsack_top_down_alt(items, total_weight):
    if items is None or total_weight is None:
        raise TypeError('input_items or total_weight cannot be None')
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
        weight=memo[(total_weight,
                     len(items) - index - 1)].total_weight + items[index - 1].value
        return Result(total_weight=weight,
                      item=items[index-1])
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
    return Result(total_weight=weight,
                  item=result_item)
```

## Unit Test

```python
%%writefile test_knapsack.py
import unittest


class TestKnapsack(unittest.TestCase):

    def test_knapsack_bottom_up(self):
        knapsack = Knapsack()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results[0].label, 'd')
        self.assertEqual(results[1].label, 'b')
        total_value = 0
        for item in results:
            total_value += item.value
        self.assertEqual(total_value, expected_value)
        print('Success: test_knapsack_bottom_up')

    def test_knapsack_top_down(self):
        knapsack = KnapsackTopDown()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        self.assertEqual(knapsack.fill_knapsack(items, total_weight), expected_value)
        print('Success: test_knapsack_top_down')

def main():
    test = TestKnapsack()
    test.test_knapsack_bottom_up()
    test.test_knapsack_top_down()


if __name__ == '__main__':
    main()
```

    Overwriting test_knapsack.py

```python
%run -i test_knapsack.py
```

    Success: test_knapsack_bottom_up
    Success: test_knapsack_top_down
