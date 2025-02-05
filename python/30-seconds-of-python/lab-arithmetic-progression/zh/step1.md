# 等差数列

编写一个函数 `arithmetic_progression(n, lim)`，它接受两个正整数 `n` 和 `lim`，并返回一个从 `n` 开始到 `lim` 为止的等差数列中的数字列表。该函数应使用 `range()` 和 `list()` 以及适当的起始值、步长和结束值来生成列表。

### 输入

- 两个正整数 `n` 和 `lim`，其中 `n` 是起始数字，`lim` 是限制。

### 输出

- 一个从 `n` 开始到 `lim` 为止的等差数列中的数字列表。

```python
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
```

```python
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```
