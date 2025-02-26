# Relación "es un"

La herencia establece una relación de tipo.

```python
class Shape:
...

class Circle(Shape):
...
```

Comprueba la instancia de objeto.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_Importante: Idealmente, cualquier código que funcione con instancias de la clase padre también funcionará con instancias de la clase hija._
