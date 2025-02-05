# 使用 pandas.NA 处理缺失值

`IntegerArray` 类使用 `pandas.NA` 作为其标量缺失值。当你切片一个缺失的单个元素时，它将返回 `pandas.NA`。

```python
# 创建一个带有缺失值的 IntegerArray
a = pd.array([1, None], dtype="Int64")

# 切片第二个元素，该元素是一个缺失值
missing_value = a[1]
# 输出: <NA>
```
