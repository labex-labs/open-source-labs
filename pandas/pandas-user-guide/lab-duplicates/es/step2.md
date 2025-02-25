# Comprendiendo las consecuencias de las etiquetas duplicadas

Las etiquetas duplicadas pueden cambiar el comportamiento de ciertas operaciones en pandas. Por ejemplo, algunos métodos no funcionan cuando hay duplicados.

```python
# Creando una Serie de pandas con etiquetas duplicadas
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Intentando reindexar la Serie
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
