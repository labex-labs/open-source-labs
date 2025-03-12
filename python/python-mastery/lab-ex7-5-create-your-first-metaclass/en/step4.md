# Exploring Metaclass Inheritance

An interesting property of metaclasses is that they are "sticky" - they propagate through inheritance hierarchies. This means that subclasses of a class with a metaclass will also use that metaclass.

Let's see this in action:

1. Open `mymeta.py` and add the following code at the end of the file:

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. Save the file.

3. Let's create a new file named `test_inheritance.py` to test this inheritance behavior:

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

4. Run this file to see the metaclass in action through inheritance:

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

Notice how the metaclass is also applied to `MyStock`, even though we didn't explicitly specify it. This demonstrates how metaclasses propagate through inheritance.

## Practical Uses of Metaclasses

While this example simply prints information about classes, metaclasses have many practical applications:

1. **Validation**: Checking that a class has required methods or attributes
2. **Registration**: Automatically registering classes in a registry
3. **Interface enforcement**: Ensuring classes implement required interfaces
4. **Aspect-oriented programming**: Adding behaviors to methods
5. **ORM systems**: Mapping classes to database tables (like in Django or SQLAlchemy)

Metaclasses are powerful but should be used sparingly. As Tim Peters (of Zen of Python fame) once said, "Metaclasses are deeper magic than 99% of users should ever worry about."
