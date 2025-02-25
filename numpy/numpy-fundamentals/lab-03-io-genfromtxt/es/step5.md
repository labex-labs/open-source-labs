# Estableciendo el tipo de datos

El argumento `dtype` se utiliza para controlar cómo se convierten las cadenas a otros tipos. Puede ser un solo tipo, una secuencia de tipos, una cadena separada por comas, un diccionario, una secuencia de tuplas, un objeto `numpy.dtype` existente o `None` para determinar el tipo a partir de los datos mismos.

```python
np.genfromtxt(StringIO(data), dtype=float)
```
