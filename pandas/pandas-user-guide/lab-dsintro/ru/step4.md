# Обработка столбцов DataFrame

Вы можете выполнять различные операции с столбцами DataFrame. Например, можно выбрать столбец, добавить новый столбец или удалить столбец.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
