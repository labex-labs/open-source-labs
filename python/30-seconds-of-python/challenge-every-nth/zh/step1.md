# 列表中的每隔 n 个元素

## 问题

编写一个函数 `every_nth(lst, nth)`，它接受一个列表 `lst` 和一个整数 `nth` 作为参数，并返回一个新列表，该新列表包含原始列表中的每隔 `n` 个元素。

## 示例

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```

## 约束条件

- 输入列表 `lst` 至少包含 `nth` 个元素。
- `nth` 的值将大于 0。
