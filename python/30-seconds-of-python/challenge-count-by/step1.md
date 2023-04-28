# Count Grouped Elements

## Problem

Write a function `count_by(lst, fn = lambda x: x)` that takes a list `lst` and a function `fn` as arguments. The function should group the elements of the list based on the given function and return a dictionary with the count of elements in each group.

To solve this problem, you can follow these steps:

1. Initialize a dictionary using `collections.defaultdict`.
2. Use `map()` to apply the given function to each element of the list.
3. Iterate over the mapped values and increase the count of each element in the dictionary.

The function should return the resulting dictionary.

## Example

```py
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```

In the first example, the function `floor` is used to group the elements of the list `[6.1, 4.2, 6.3]`. The resulting dictionary has two keys: `6` and `4`, with values `2` and `1`, respectively.

In the second example, the function `len` is used to group the elements of the list `['one', 'two', 'three']`. The resulting dictionary has two keys: `3` and `5`, with values `2` and `1`, respectively.
