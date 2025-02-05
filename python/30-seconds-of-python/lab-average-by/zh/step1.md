# 映射列表的平均值

编写一个名为 `average_by(lst, fn = lambda x: x)` 的函数，该函数接受一个列表 `lst` 和一个函数 `fn` 作为参数。函数 `fn` 应用于列表的每个元素，将其映射为一个值。然后，该函数应计算这些映射值的平均值并返回。

如果未提供 `fn` 参数，函数应使用默认的恒等函数，该函数直接返回元素本身。

你的函数应满足以下要求：

- 使用 `map()` 将每个元素映射为 `fn` 返回的值。
- 使用 `sum()` 对所有映射值求和，再除以 `len(lst)`。
- 省略最后一个参数 `fn` 以使用默认的恒等函数。

函数签名：`def average_by(lst, fn = lambda x: x) -> float:`

```python
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```python
average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
# 5.0
```
