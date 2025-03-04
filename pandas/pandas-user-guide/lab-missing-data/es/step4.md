# Realizar cálculos con datos faltantes

Realizaremos algunos cálculos aritméticos y estadísticos con datos faltantes.

```python
# Realizar cálculos con datos faltantes
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```
