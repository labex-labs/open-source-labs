# 斐波那契数列

编写一个名为 `fibonacci(n)` 的函数，该函数接受一个整数 `n` 作为参数，并返回一个包含直到第 `n` 项的斐波那契数列的列表。

要解决这个问题，你可以按照以下步骤进行：

1. 创建一个名为 `sequence` 的空列表。
2. 如果 `n` 小于或等于0，则将0添加到 `sequence` 列表中并返回该列表。
3. 将0和1添加到 `sequence` 列表中。
4. 使用 `while` 循环将 `sequence` 列表中最后两个数字的和添加到列表末尾，直到列表长度达到 `n`。
5. 返回 `sequence` 列表。

```python
def fibonacci(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
```

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
