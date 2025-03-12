# Exploring Metaclass Inheritance

Metaclasses have a fascinating characteristic: they are "sticky". This means that once a class uses a metaclass, all its subclasses in the inheritance hierarchy will also use the same metaclass. In other words, the metaclass property propagates through the inheritance chain.

Let's see this in action:

1. First, open the `mymeta.py` file. At the end of this file, we're going to add a new class. This class, named `MyStock`, will inherit from the `Stock` class. The `__init__` method is used to initialize the object's attributes, and we call the `__init__` method of the parent class using `super().__init__` to initialize the common attributes. The `info` method is used to return a formatted string with information about the stock. Add the following code:

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. After adding the code, save the `mymeta.py` file. Saving the file ensures that the changes we made are stored and can be used later.

3. Now, we'll create a new file named `test_inheritance.py` to test the inheritance behavior of the metaclass. In this file, we'll import the `MyStock` class from the `mymeta.py` file. Then, we'll create an instance of the `MyStock` class, call its methods, and print the results to see how the metaclass works through inheritance. Add the following code to `test_inheritance.py`:

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. Finally, run the `test_inheritance.py` file to see the metaclass in action through inheritance. Open your terminal, navigate to the directory where the `test_inheritance.py` file is located, and run the following command:

```bash
python3 test_inheritance.py
```

You should see output similar to:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

Notice that even though we didn't explicitly specify a metaclass for the `MyStock` class, the metaclass is still applied. This clearly demonstrates how metaclasses propagate through inheritance.

## Practical Uses of Metaclasses

In our example, the metaclass simply prints information about classes. However, metaclasses have many practical applications in real - world programming:

1. **Validation**: You can use metaclasses to check if a class has the required methods or attributes. This helps ensure that classes meet certain criteria before they are used.
2. **Registration**: Metaclasses can automatically register classes in a registry. This is useful when you need to keep track of all the classes of a certain type.
3. **Interface enforcement**: They can be used to ensure that classes implement required interfaces. This helps maintain a consistent structure in your code.
4. **Aspect - oriented programming**: Metaclasses can add behaviors to methods. For example, you can add logging or performance monitoring to methods without modifying the method code directly.
5. **ORM systems**: In Object - Relational Mapping (ORM) systems like Django or SQLAlchemy, metaclasses are used to map classes to database tables. This simplifies database operations in your application.

Metaclasses are very powerful, but they should be used sparingly. As Tim Peters (famous for the Zen of Python) once said, "Metaclasses are deeper magic than 99% of users should ever worry about."
