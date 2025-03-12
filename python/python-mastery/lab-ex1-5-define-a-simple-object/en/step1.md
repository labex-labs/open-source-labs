# Understanding Python Classes

In Python, a class serves as a blueprint for creating objects. Object-oriented programming is a powerful approach that enables us to organize our code effectively. It does this by grouping related data and functions together. This way, we can manage complex programs more easily and make our code more modular and maintainable.

A Python class is made up of two main components:

- **Attributes**: These are variables that store data within a class. Think of attributes as the characteristics or properties of an object. For example, if we are creating a class to represent a person, attributes could be the person's name, age, and height.
- **Methods**: These are functions that belong to a class and can access or modify its attributes. Methods define the actions that an object can perform. Using the person class example, a method could be a function that calculates the person's age in months.

Classes are extremely useful as they provide a way to create reusable code and model real-world concepts. In this lab, we will create a `Stock` class. This class will be used to represent stock information such as the name of the stock, the number of shares, and the price per share.

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

The `__init__` method is a special method in Python classes. It is called automatically when we create a new object from the class. This method is used to initialize the object's attributes. The `self` parameter is a reference to the instance of the class. It is used to access attributes and methods from within the class. When we call a method on an object, Python automatically passes the object itself as the first argument, which is why we use `self` in the method definitions. This allows us to work with the specific instance's attributes and perform operations on them.
