# Manipulating DataFrame Columns

You can perform various operations on DataFrame columns. For example, you can select a column, add a new column, or delete a column.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
