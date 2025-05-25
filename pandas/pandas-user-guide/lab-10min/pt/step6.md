# Operações com Dados

Podemos realizar operações em dataframes, como ordenação, aplicação de funções, etc.

```python
# Sorting by an axis
df.sort_index(axis=1, ascending=False)

# Applying a function to the data
df.apply(np.cumsum)
```
