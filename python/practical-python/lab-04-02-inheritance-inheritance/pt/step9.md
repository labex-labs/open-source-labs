# Relação "é um" ("is a")

A herança estabelece uma relação de tipo.

```python
class Shape:
    ...

class Circle(Shape):
    ...
```

Verifique a instância do objeto.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_Importante: Idealmente, qualquer código que funcionasse com instâncias da classe pai também funcionará com instâncias da classe filha._
