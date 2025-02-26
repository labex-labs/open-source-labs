# Clase base `object`

Si una clase no tiene un padre, a veces se ve que se utiliza `object` como base.

```python
class Shape(object):
...
```

`object` es el padre de todos los objetos en Python.

\*Nota: técnicamente no es necesario, pero a menudo se ve especificado como un vestigio de su uso obligatorio en Python 2. Si se omite, la clase todavía hereda implícitamente de `object`.
