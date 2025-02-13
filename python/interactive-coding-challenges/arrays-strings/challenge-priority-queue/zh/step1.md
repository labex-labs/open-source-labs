# 优先队列

## 问题

实现一个由数组支持的优先队列。该优先队列应支持以下方法：

- `insert`：向优先队列中插入一个新元素
- `extract_min`：从优先队列中移除并返回最小元素
- `decrease_key`：降低优先队列中给定元素的键值

## 要求

为了实现优先队列，我们需要满足以下要求：

- 优先队列支持的方法应为 `insert`、`extract_min` 和 `decrease_key`。
- 优先队列中不会有任何重复的键值。
- 我们无需验证输入。
- 优先队列应能装入内存。

## 示例用法

以下是一些如何使用优先队列方法的示例：

### insert

- `insert` 一般情况：向优先队列中插入一个新节点。

### extract_min

- 从空列表中 `extract_min`：返回 `None`。
- `extract_min` 一般情况：从优先队列中移除并返回最小节点。

### decrease_key

- 对无效键值执行 `decrease_key`：返回 `None`。
- `decrease_key` 一般情况：降低优先队列中给定节点的键值。
