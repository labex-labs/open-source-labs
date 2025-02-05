# 找到所有匹配的索引

编写一个函数 `find_index_of_all(lst, fn)`，它接受一个列表 `lst` 和一个测试函数 `fn` 作为参数，并返回 `lst` 中所有使得 `fn` 返回 `True` 的元素的索引列表。

### 输入

- 一个整数列表 `lst`。
- 一个测试函数 `fn`，它接受一个整数作为输入并返回一个布尔值。

### 输出

- 一个整数列表，表示 `lst` 中所有使得 `fn` 返回 `True` 的元素的索引。

```python
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
