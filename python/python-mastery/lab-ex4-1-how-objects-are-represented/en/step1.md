# Creating a Simple Stock Class

In this step, we're going to create a simple class to represent a stock. Understanding how to create classes is fundamental in Python, as it allows us to model real - world objects and their behaviors. This simple stock class will be our starting point to explore how Python objects work internally.

To begin, we need to open a Python interactive shell. The Python interactive shell is a great place to experiment with Python code. You can type and execute Python commands one by one. To open it, type the following command in the terminal:

```bash
python3
```

Once you've entered the command, you'll see the Python prompt (`>>>`). This indicates that you're now inside the Python interactive shell and can start writing Python code.

Now, let's define a `SimpleStock` class. A class in Python is like a blueprint for creating objects. It defines the attributes (data) and methods (functions) that the objects of that class will have. Here's how you define the `SimpleStock` class with the necessary attributes and methods:

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

In the code above, the `__init__` method is a special method in Python classes. It's called a constructor, and it's used to initialize the object's attributes when an object is created. The `self` parameter refers to the instance of the class that's being created. The `cost` method calculates the total cost of the shares by multiplying the number of shares by the price per share.

After defining the class, we can create instances of the `SimpleStock` class. An instance is an actual object created from the class blueprint. Let's create two instances to represent different stocks:

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

These instances represent 100 shares of Google stock at $490.10 per share and 50 shares of IBM stock at $91.23 per share. Each instance has its own set of attribute values.

Let's verify that our instances are working properly. We can do this by checking their attributes and calculating their cost. This will help us confirm that the class and its methods are functioning as expected.

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

The `cost()` method multiplies the number of shares by the price per share to calculate the total cost of holding those shares. By running these commands, we can see that the instances have the correct attribute values and that the `cost` method is calculating the cost accurately.
