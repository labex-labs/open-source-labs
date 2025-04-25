# 检查和设置重复标签标志

最后，我们可以检查并设置 DataFrame 上的`allows_duplicate_labels`标志。

```python
# 创建一个 DataFrame 并将 allows_duplicate_labels 设置为 False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# 检查 allows_duplicate_labels 标志
print(df.flags.allows_duplicate_labels)

# 将 allows_duplicate_labels 设置为 True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
