# Group List Elements

Write a function `group_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments and returns a dictionary where the keys are the results of applying `fn` to the elements of `lst` and the values are lists of elements from `lst` that produce the corresponding key when `fn` is applied to them.

For example, if we have a list of numbers `[6.1, 4.2, 6.3]` and we want to group them by their integer part, we can use the `floor` function from the `math` module as the grouping function. The expected output would be `{4: [4.2], 6: [6.1, 6.3]}`.

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
