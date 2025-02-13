# 展开列表

## 问题

你的任务是实现 `unfold` 函数，该函数接受一个迭代器函数和一个初始种子值作为参数。迭代器函数接受一个参数（`seed`），并且必须始终返回一个包含两个元素的列表（`[value, nextSeed]`）或 `False` 以终止。`unfold` 函数应该使用一个生成器函数 `fn_generator`，该函数使用 `while` 循环调用迭代器函数并 `yield` 出 `value`，直到它返回 `False`。最后，`unfold` 函数应该使用列表推导式返回由生成器生成的列表，使用迭代器函数。

实现 `unfold` 函数：

```python
def unfold(fn, seed):
    # 你的代码在这里
```

### 输入

- 一个迭代器函数 `fn`，它接受一个参数（`seed`），并且必须始终返回一个包含两个元素的列表（`[value, nextSeed]`）或 `False` 以终止。
- 一个初始种子值 `seed`。

### 输出

- 一个由生成器生成的列表，使用迭代器函数。

## 示例

```python
f = lambda n: False if n > 50 else [-n, n + 10]
assert unfold(f, 10) == [-10, -20, -30, -40, -50]
```
