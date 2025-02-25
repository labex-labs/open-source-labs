# Crear puntos de datos

En este paso, crearemos algunos puntos de datos usando la clase de unidad personalizada - `Foo`.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
