# "is a" relationship

Inheritance establishes a type relationship.

```python
class Shape:
    ...

class Circle(Shape):
    ...
```

Check for object instance.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_Important: Ideally, any code that worked with instances of the parent
class will also work with instances of the child class._
