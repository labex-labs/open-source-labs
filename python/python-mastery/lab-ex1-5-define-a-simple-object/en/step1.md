# Understanding Python Classes

In Python, a class is a blueprint for creating objects. Object-oriented programming allows us to organize code by grouping related data and functions together.

A Python class consists of:

- **Attributes**: Variables that store data within a class
- **Methods**: Functions that belong to a class and can access or modify its attributes

Classes provide a way to create reusable code and model real-world concepts. In this lab, we will create a `Stock` class to represent stock information such as name, number of shares, and price per share.

Here is the basic structure of a Python class:

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method_name(self):
        # Code that uses the attributes
        return result
```

The `__init__` method is a special method called when creating new objects. The `self` parameter refers to the instance of the class and is used to access attributes and methods from within the class.
