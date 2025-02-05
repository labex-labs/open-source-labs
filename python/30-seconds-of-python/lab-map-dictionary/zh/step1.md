# 将列表映射到字典

编写一个名为 `map_dictionary(itr, fn)` 的 Python 函数，该函数接受两个参数：

- `itr`：一个值列表
- `fn`：一个函数，该函数接受一个值作为输入并返回一个值作为输出

该函数应返回一个字典，其中键值对由原始值作为键，函数的结果作为值组成。

要解决此问题，请执行以下步骤：

1. 使用 `map()` 将 `fn` 应用于列表的每个值。
2. 使用 `zip()` 将原始值与 `fn` 产生的值配对。
3. 使用 `dict()` 返回一个适当的字典。

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
