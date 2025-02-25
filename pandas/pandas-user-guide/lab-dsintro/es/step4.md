# Manipulando columnas de DataFrame

Puedes realizar diversas operaciones en las columnas de un DataFrame. Por ejemplo, puedes seleccionar una columna, agregar una nueva columna o eliminar una columna.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
