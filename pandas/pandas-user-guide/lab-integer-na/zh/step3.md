# 对可空整数数组执行操作

你可以对可空整数数组执行各种操作，例如算术运算、比较和切片。

```python
# 创建一个具有可空整数类型的 Series
s = pd.Series([1, 2, None], dtype="Int64")

# 执行算术运算
s_plus_one = s + 1 # 将 1 添加到 Series 中的每个元素

# 执行比较
comparison = s == 1 # 检查 Series 中的每个元素是否等于 1

# 执行切片操作
sliced = s.iloc[1:3] # 选择 Series 中的第二个和第三个元素
```
