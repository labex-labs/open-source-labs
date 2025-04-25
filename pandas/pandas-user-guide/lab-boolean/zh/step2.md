# 使用 NA 值进行索引

Pandas 允许在布尔数组中使用`NA`值进行索引，这些值被视为`False`。

```python
# 创建一个 pandas Series
s = pd.Series([1, 2, 3])

# 创建一个包含 NA 值的布尔数组
mask = pd.array([True, False, pd.NA], dtype="boolean")

# 使用布尔数组对 Series 进行索引
s[mask] # NA 值被视为 False
```

如果你想保留`NA`值，可以手动用`fillna(True)`填充它们。

```python
# 用 True 填充 NA 值并对 Series 进行索引
s[mask.fillna(True)]
```
