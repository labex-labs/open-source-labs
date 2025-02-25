# Duplicados en el índice

A continuación, veremos cómo los duplicados en el índice pueden conducir a resultados inesperados.

```python
# Creando un DataFrame con etiquetas de columna duplicadas
df1 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "A", "B"])

# Indexando 'B' devuelve una Serie
print(df1["B"])

# Indexando 'A' devuelve un DataFrame
print(df1["A"])
```
