# 2 的幂

## 问题

编写一个名为 `is_power_of_two` 的 Python 函数，该函数接受一个整数作为参数，如果输入是 2 的幂，则返回 `True`，否则返回 `False`。2 的幂是任何可以表示为 2^n 的数，其中 n 是整数。例如，2、4、8 和 16 都是 2 的幂。

## 要求

`is_power_of_two` 函数必须满足以下要求：

- 输入数字必须是整数。
- 函数必须优雅地处理无效输入。
- 输出必须是布尔值。
- 函数必须符合内存限制。

## 示例用法

以下是 `is_power_of_two` 函数应有的行为示例：

- `is_power_of_two(None)` 应引发 `TypeError`。
- `is_power_of_two(0)` 应返回 `False`。
- `is_power_of_two(1)` 应返回 `True`。
- `is_power_of_two(2)` 应返回 `True`。
- `is_power_of_two(15)` 应返回 `False`。
- `is_power_of_two(16)` 应返回 `True`。
