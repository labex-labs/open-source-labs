# Creación de un array de registros

Un array de registros es una subclase de `ndarray` que permite el acceso a los campos por atributo en lugar de por índice. Podemos crear un array de registros utilizando la función `np.rec.array`.

```python
# Crea un array de registros
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
