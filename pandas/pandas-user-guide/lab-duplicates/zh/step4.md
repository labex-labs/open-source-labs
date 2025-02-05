# 检测重复标签

我们可以使用`Index.is_unique`和`Index.duplicated()`方法来检查重复标签。

```python
# 检查索引是否具有唯一标签
print(df1.index.is_unique)

# 检查列是否具有唯一标签
print(df1.columns.is_unique)

# 检测索引中的重复标签
print(df1.index.duplicated())
```
