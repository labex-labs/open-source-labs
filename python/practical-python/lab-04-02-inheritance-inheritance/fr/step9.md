# Relation "est un"

L'héritage établit une relation de type.

```python
class Shape:
...

class Circle(Shape):
...
```

Vérifiez l'instance d'objet.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_Important : Idéalement, tout code qui fonctionnait avec des instances de la classe parent fonctionnera également avec des instances de la classe enfant._
