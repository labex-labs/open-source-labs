# 找出奇偶性异常值

## 问题

编写一个函数 `find_parity_outliers(nums)`，它接受一个整数列表 `nums` 作为参数，并返回 `nums` 中所有的奇偶性异常值列表。

要解决这个问题，你可以按照以下步骤进行：

1. 使用 `collections.Counter` 和列表推导式来统计列表中偶数和奇数的值。
2. 使用 `collections.Counter.most_common()` 来获取最常见的奇偶性。
3. 使用列表推导式来找出所有与最常见奇偶性不匹配的元素。

## 示例

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```

在上述示例中，列表中的大多数元素是偶数，因此奇偶性异常值是奇数元素 1 和 3。
