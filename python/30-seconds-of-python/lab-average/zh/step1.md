# 平均值

编写一个名为 `average` 的函数，该函数接受两个或更多数字并返回它们的平均值。你的函数应遵循以下准则：

- 使用 `sum()` 对提供的所有 `args` 进行求和，再除以 `len()`。
- 该函数应能够处理任意数量的参数。
- 该函数应返回一个浮点数。

```python
def average(*args):
  return sum(args, 0.0) / len(args)
```

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
