# Get Nested Value

Write a function `get(d, selectors)` that takes a dictionary or list `d` and a list of selectors `selectors` as arguments and returns the value of the nested key indicated by the given selector list. If the key does not exist, return `None`.

To implement this function, use `functools.reduce()` to iterate over the `selectors` list. Apply `operator.getitem()` for each key in `selectors`, retrieving the value to be used as the iteratee for the next iteration.

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```
