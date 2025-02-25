# DataFrame の列を操作する

DataFrame の列に対して様々な操作を行うことができます。たとえば、列を選択したり、新しい列を追加したり、列を削除したりすることができます。

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
