# 操作 DataFrame 的列

你可以对 DataFrame 的列执行各种操作。例如，你可以选择一列、添加新列或删除列。

```python
# 选择列 A
df['A']

# 添加新列 E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# 删除列 B
del df['B']
```
