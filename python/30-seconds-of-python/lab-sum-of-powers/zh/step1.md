# 幂之和

编写一个名为 `sum_of_powers` 的 Python 函数，它接受三个参数：

- `end` - 一个整数，表示范围的结束值（包含该值）
- `power` - 一个整数，表示范围内每个数字应被提升到的幂（默认值为 2）
- `start` - 一个整数，表示范围的起始值（默认值为 1）

该函数应返回从 `start` 到 `end`（包含两端）的所有数字的幂之和。

要解决这个问题，你可以按照以下步骤进行：

1. 将 `range()` 与列表推导式结合使用，创建一个包含所需范围内数字提升到给定 `power` 的列表。
2. 使用 `sum()` 将这些值相加。

```python
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```python
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```
