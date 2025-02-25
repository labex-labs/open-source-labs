# Insertar datos faltantes

Aquí, veremos cómo insertar valores faltantes en nuestros datos.

```python
# Insertar valores faltantes
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
