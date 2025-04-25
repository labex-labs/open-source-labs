# 使用稀疏访问器

我们可以使用 `.sparse` 访问器来获取特定于稀疏数据的属性和方法。

```python
# 创建一个具有稀疏值的 Series
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# 使用稀疏访问器
print(s.sparse.density)
print(s.sparse.fill_value)
```
