# 使用NA值进行索引

Pandas允许在布尔数组中使用`NA`值进行索引，这些值被视为`False`。

```python
# 创建一个pandas Series
s = pd.Series([1, 2, 3])

# 创建一个包含NA值的布尔数组
mask = pd.array([True, False, pd.NA], dtype="boolean")

# 使用布尔数组对Series进行索引
s[mask] # NA值被视为False
```

如果你想保留`NA`值，可以手动用`fillna(True)`填充它们。

```python
# 用True填充NA值并对Series进行索引
s[mask.fillna(True)]
```
