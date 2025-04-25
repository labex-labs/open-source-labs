# 使用字符串方法

Pandas 提供了一套字符串处理方法，便于对字符串数据进行操作。这些方法会自动排除缺失/NA 值。

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# 转换为小写
s.str.lower()

# 转换为大写
s.str.upper()

# 计算每个字符串的长度
s.str.len()
```
