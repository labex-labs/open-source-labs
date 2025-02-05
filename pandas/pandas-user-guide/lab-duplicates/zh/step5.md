# 禁止重复标签

如果需要，我们可以通过使用`set_flags(allows_duplicate_labels=False)`方法来禁止重复标签。

```python
# 在Series中禁止重复标签
try:
    pd.Series([0, 1, 2], index=["a", "b", "b"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)

# 在DataFrame中禁止重复标签
try:
    pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "B", "C"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)
```
