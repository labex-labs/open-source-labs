# Listas y matemáticas

_Advertencia: Las listas no fueron diseñadas para operaciones matemáticas._

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

Especificamente, las listas no representan vectores/matrices como en MATLAB, Octave, R, etc. Sin embargo, hay algunos paquetes que pueden ayudarte en eso (por ejemplo, [numpy](https://numpy.org)).

En este ejercicio, experimentamos con el tipo de datos de lista de Python. En la última sección, trabajaste con cadenas que contenían símbolos de acciones.

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

Divídelo en una lista de nombres utilizando la operación `split()` de cadenas:

```python
>>> symlist = symbols.split(',')
```
