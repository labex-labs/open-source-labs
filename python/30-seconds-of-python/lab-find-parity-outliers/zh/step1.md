# 找出奇偶性异常值

编写一个函数 `find_parity_outliers(nums)`，它接受一个整数列表 `nums` 作为参数，并返回 `nums` 中所有奇偶性异常值的列表。

要解决这个问题，你可以按照以下步骤进行：

1. 使用 `collections.Counter` 和列表推导式来统计列表中偶数和奇数的值。
2. 使用 `collections.Counter.most_common()` 来获取最常见的奇偶性。
3. 使用列表推导式来找出所有与最常见奇偶性不匹配的元素。

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2!= Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
