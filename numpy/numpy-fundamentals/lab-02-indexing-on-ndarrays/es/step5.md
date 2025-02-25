# Acceso a Campos

Si el objeto ndarray es un array estructurado, los campos del array se pueden acceder indexando el array con cadenas, de forma similar a un diccionario.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Salida: [1, 3, 5]
```
