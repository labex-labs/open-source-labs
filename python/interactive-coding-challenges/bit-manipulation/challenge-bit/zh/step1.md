# 位操作

## 问题

在 Python 中实现以下常见的位操作：

- `get_bit`：给定一个数字和一个索引，返回给定索引处的位值。
- `set_bit`：给定一个数字和一个索引，将给定索引处的位值设置为 1。
- `clear_bit`：给定一个数字和一个索引，将给定索引处的位值设置为 0。
- `clear_bits_msb_to_index`：给定一个数字和一个索引，将从最高有效位到给定索引的所有位设置为 0。
- `clear_bits_index_to_lsb`：给定一个数字和一个索引，将从给定索引到最低有效位的所有位设置为 0。
- `update_bit`：给定一个数字、一个索引和一个值，将给定索引处的位值更新为给定值。

## 要求

实现应满足以下要求：

- 输入可能无效，实现应能优雅地处理此类情况。
- 实现应符合内存要求。

## 示例用法

以下是如何使用实现的函数的一些示例：

- `get_bit`：
  ```
  number   = 0b10001110
  index = 3
  expected = True
  ```
- `set_bit`：
  ```
  number   = 0b10001110
  index = 4
  expected = 0b10011110
  ```
- `clear_bit`：
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000110
  ```
- `clear_bits_msb_to_index`：
  ```
  number   = 0b10001110
  index = 3
  expected = 0b00000110
  ```
- `clear_bits_index_to_lsb`：
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000000
  ```
- `update_bit`：

  ```
  number   = 0b10001110
  index = 3
  value = 1
  expected = 0b10001110

  number   = 0b10001110
  index = 3
  value = 0
  expected = 0b10000110

  number   = 0b10001110
  index = 0
  value = 1
  expected = 0b10001111
  ```
