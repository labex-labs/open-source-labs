# 数学运算

## 问题

创建一个 Python 类，该类具有一个插入方法，可将整数插入列表。该类还应支持在 O(1) 时间复杂度内计算列表的最大值、最小值、平均值和众数。该类应处理以下情况：

- 如果输入无效，应引发 `TypeError`。
- 如果列表为空，应引发 `ValueError`。
- 如果存在多个众数，可以返回其中任何一个众数。

## 要求

为了解决上述问题，我们需要遵循以下要求：

- 输入可能无效，因此我们不能假设输入是有效的。
- 输入范围在 0 到 100（包括 0 和 100）之间。
- 平均值应返回浮点数。
- 其他结果应返回整数。
- 如果存在多个众数，该类可以返回其中任何一个众数。
- 我们可以假设列表能够装入内存。

## 示例用法

以下是一些使用该类的示例：

- 无 -> `TypeError`
- [] -> `ValueError`
- [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
  - 最大值：9
  - 最小值：2
  - 平均值：4.909090909090909
  - 众数：9 或 2
