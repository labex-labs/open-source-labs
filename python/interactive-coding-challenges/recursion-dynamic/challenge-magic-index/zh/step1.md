# 神奇索引

## 问题

给定一个可能包含重复元素的有序整数数组，编写一个 Python 函数来找到数组中的神奇索引（如果存在）。如果有多个神奇值，则返回最左边的那个。如果没有神奇索引，则返回 -1。

## 要求

为了解决这个问题，必须满足以下要求：

- 数组是有序的。
- 数组中的元素可能不唯一。
- 数组中允许有负数。
- 如果没有神奇索引，则返回 -1。

## 示例用法

以下示例说明了该函数的用法：

- 无输入 -> -1
- 空数组 -> -1

```txt
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

结果：2

```txt
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

结果：6

```txt
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
```

结果：-1
