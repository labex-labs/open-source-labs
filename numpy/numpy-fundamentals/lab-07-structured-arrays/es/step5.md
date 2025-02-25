# Comparando arrays estructurados

Si los tipos de datos (`dtypes`) de dos arrays estructurados son iguales, podemos compararlos utilizando el operador de igualdad (`==`). Esto devolverá un array booleano que indica qué elementos tienen los mismos valores para todos los campos.

```python
# Compara dos arrays estructurados
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
