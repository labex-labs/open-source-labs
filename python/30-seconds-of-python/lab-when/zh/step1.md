# 条件为真时应用函数

编写一个名为 `when` 的函数，它接受两个参数：一个谓词函数 `predicate` 和一个在条件为真时要应用的函数 `when_true`。`when` 函数应返回一个新函数，该新函数接受单个参数 `x`。这个新函数应检查 `predicate(x)` 的值是否为 `True`。如果是，新函数应调用 `when_true(x)` 并返回结果。否则，新函数应返回 `x`。

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
