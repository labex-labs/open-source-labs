# 获取嵌套值

编写一个函数 `get(d, selectors)`，它接受一个字典或列表 `d` 和一个选择器列表 `selectors` 作为参数，并返回由给定选择器列表指示的嵌套键的值。如果键不存在，则返回 `None`。

要实现此函数，请使用 `functools.reduce()` 遍历 `selectors` 列表。对 `selectors` 中的每个键应用 `operator.getitem()`，获取要用作下一次迭代的迭代值的值。

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
