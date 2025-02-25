# Detectando etiquetas duplicadas

Podemos comprobar si hay etiquetas duplicadas utilizando los métodos `Index.is_unique` y `Index.duplicated()`.

```python
# Comprobando si el índice tiene etiquetas únicas
print(df1.index.is_unique)

# Comprobando si las columnas tienen etiquetas únicas
print(df1.columns.is_unique)

# Detectando etiquetas duplicadas en el índice
print(df1.index.duplicated())
```
