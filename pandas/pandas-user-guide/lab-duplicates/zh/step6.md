# 检查和设置重复标签标志

最后，我们可以检查并设置DataFrame上的`allows_duplicate_labels`标志。

```python
# 创建一个DataFrame并将allows_duplicate_labels设置为False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# 检查allows_duplicate_labels标志
print(df.flags.allows_duplicate_labels)

# 将allows_duplicate_labels设置为True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
