# Using Inheritance

Inheritance is sometimes used to organize related objects.

```python
class Shape:
    ...

class Circle(Shape):
    ...

class Rectangle(Shape):
    ...
```

Think of a logical hierarchy or taxonomy. However, a more common (and practical) usage is related to making reusable or extensible code. For example, a framework might define a base class and instruct you to customize it.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
        ...
        # Custom processing
```

The base class contains some general purpose code. Your class inherits and customized specific parts.
