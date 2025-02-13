# 生成质数

## 问题

编写一个 Python 函数，用于生成质数列表。该函数应以整数作为输入，并返回一个布尔值列表，其中每个值对应于该索引处的数是否为质数。例如，如果输入为 20，输出应为 [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]，其中索引 2 处的值为 True，因为 2 是质数，而索引 4 处的值为 False，因为 4 不是质数。

## 要求

- 该函数不应将 1 视为质数。
- 该函数应通过引发异常来处理无效输入。
- 该函数应在内存中生成质数列表。

## 示例用法

- 无 -> 异常
- 不是整数 -> 异常
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
