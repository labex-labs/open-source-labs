# Manipulando Colunas do DataFrame

Você pode realizar várias operações nas colunas do DataFrame. Por exemplo, você pode selecionar uma coluna, adicionar uma nova coluna ou excluir uma coluna.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
