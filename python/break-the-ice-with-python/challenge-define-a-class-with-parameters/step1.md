# Define a Class with Parameters

Define a class named `Car`, which have a class parameter named `name` and have a same instance parameter.

## Example

The following is one such class:

```python
class Car:
    name = "Car"

    def __init__(self, name=None):
        pass
```

## Hints

- Define an instance parameter, need add it in `__init__` method.You can init an object with construct parameter or set the value later.
