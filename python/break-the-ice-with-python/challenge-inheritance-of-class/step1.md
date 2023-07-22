# Inheritance of Class

Define a class named `Shape` and its subclass `Square`. The `Square` class has an init function which takes a length as argument. Both classes have a `area` function which can print the area of the shape where `Shape`'s area is 0 by default.

## Example

The following is a class named `Shape`:

```python
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0
```

## Hints

- To override a method in super class, we can define a method with the same name in the super class.
