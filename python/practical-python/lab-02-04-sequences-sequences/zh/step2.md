# 切片

切片是指从一个序列中取出一个子序列。语法是 `s[start:end]`。其中 `start` 和 `end` 是你想要的子序列的索引。

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

- 索引 `start` 和 `end` 必须是整数。
- 切片**不**包括结束值。这类似于数学中的半开区间。
- 如果省略索引，它们默认为列表的开头或结尾。
